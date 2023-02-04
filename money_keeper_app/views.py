from django.shortcuts import render, redirect
from .forms import NewAccountForm, UpdAccountForm, \
    NewIncomeTypeForm, NewIncomeForm, UpdIncomeForm, \
    NewExpenseTypeForm, NewExpenseForm, UpdExpenseForm
from .models import Payment, Account, IncomeType, ExpenseType


# def dashboard(request):
#     return render(request, "base.html")
def dashboard(request):
    if not request.user.is_authenticated:
        # если неавторизован
        return render(request, "base.html")
    accounts = Account.objects.filter(user=request.user)
    if not accounts:
        # если у пользователя нет счетов
        return render(request, "base.html")
    return render(request, "money_keeper_app/accounts_list.html", {"accounts": accounts})


def delete(request, pk):
    account = Account.objects.get(pk=pk)
    account.delete()
    return redirect("money_keeper_app:dashboard")


def account_page(request, pk):
    if not request.user.is_authenticated:
        # если неавторизован
        return render(request, "base.html")
    account = Account.objects.get(pk=pk)
    payments = Payment.objects.filter(account=account.id).order_by("-created_at")
    return render(request, "money_keeper_app/account.html", {"account": account, "payments": payments})


def add_account(request):
    if not request.user.is_authenticated:
        # если неавторизован
        return render(request, "base.html")
    form = NewAccountForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        account = form.save(commit=False)
        account.user = request.user
        account.save()
        return redirect("money_keeper_app:dashboard")
    return render(request, "money_keeper_app/add_account.html", {"form": form})


def upd_account(request, pk):
    if not request.user.is_authenticated:
        # если неавторизован
        return render(request, "base.html")
    account_instance = Account.objects.get(pk=pk)
    form = UpdAccountForm(request.POST or None, instance=account_instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("money_keeper_app:dashboard")
    return render(request, "money_keeper_app/upd_account.html", {"form": form})


def income_list(request, pk):
    if not request.user.is_authenticated:
        # если неавторизован
        return render(request, "base.html")
    account = Account.objects.get(pk=pk)
    incomes = Payment.objects.filter(account=account.id, expense=None).order_by("-created_at")
    return render(request, "money_keeper_app/income_list.html", {"account": account, "incomes": incomes})


def add_income_type(request):
    if not request.user.is_authenticated:
        # если неавторизован
        return render(request, "base.html")
    form = NewIncomeTypeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        IncomeType.objects.create(
            income_type=form.cleaned_data['income_type']
        )
        return redirect("money_keeper_app:dashboard")
    return render(request, "money_keeper_app/add_income_type.html", {"form": form})


def add_income(request, pk):
    if not request.user.is_authenticated:
        return render(request, "base.html")

    if request.method == "POST":
        form = NewIncomeForm(request.POST)
        if form.is_valid():
            income_type = form.cleaned_data["income_type"]
            account = Account.objects.get(pk=pk)
            account.amount += form.cleaned_data['count']
            account.save()
            Payment.objects.create(
                account=Account.objects.get(pk=pk),
                income=income_type,
                count=form.cleaned_data['count'],
                expense=None
            )
            return redirect("money_keeper_app:account", pk=pk)
    else:
        form = NewIncomeForm()
    return render(request, "money_keeper_app/add_income.html", {"form": form})


def upd_income(request, pk_account, pk_payment):
    if not request.user.is_authenticated:
        # если неавторизован
        return render(request, "base.html")
    income_instance = Payment.objects.get(pk=pk_payment)
    account = Account.objects.get(pk=pk_account)
    account.amount -= income_instance.count
    form = UpdIncomeForm(request.POST or None, instance=income_instance)
    if request.method == "POST" and form.is_valid():
        account.amount += form.cleaned_data['count']
        account.save()
        form.save()
        return redirect("money_keeper_app:account", pk=pk_account)
    return render(request, "money_keeper_app/upd_income.html", {"form": form})


def delete_income(request, pk_account, pk_payment):
    income = Payment.objects.get(pk=pk_payment)
    account = Account.objects.get(pk=pk_account)
    account.amount -= income.count
    account.save()
    income.delete()
    return redirect("money_keeper_app:account", pk=pk_account)


def expense_list(request, pk):
    if not request.user.is_authenticated:
        # если неавторизован
        return render(request, "base.html")
    account = Account.objects.get(pk=pk)
    expenses = Payment.objects.filter(account=account.id, income=None).order_by("-created_at")
    return render(request, "money_keeper_app/expense_list.html", {"account": account, "expenses": expenses})


def add_expense_type(request):
    if not request.user.is_authenticated:
        # если неавторизован
        return render(request, "base.html")
    form = NewExpenseTypeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        ExpenseType.objects.create(
            expense_type=form.cleaned_data['expense_type']
        )
        return redirect("money_keeper_app:dashboard")
    return render(request, "money_keeper_app/add_expense_type.html", {"form": form})


def add_expense(request, pk):
    if not request.user.is_authenticated:
        return render(request, "base.html")

    if request.method == "POST":
        form = NewExpenseForm(request.POST)
        if form.is_valid():
            expense_type = form.cleaned_data["expense_type"]
            account = Account.objects.get(pk=pk)
            account.amount -= form.cleaned_data['count']
            account.save()
            Payment.objects.create(
                account=Account.objects.get(pk=pk),
                income=None,
                count=form.cleaned_data['count'],
                expense=expense_type
            )
            return redirect("money_keeper_app:account", pk=pk)
    else:
        form = NewExpenseForm()
    return render(request, "money_keeper_app/add_expense.html", {"form": form})


def upd_expense(request, pk_account, pk_payment):
    if not request.user.is_authenticated:
        # если неавторизован
        return render(request, "base.html")
    expense_instance = Payment.objects.get(pk=pk_payment)
    account = Account.objects.get(pk=pk_account)
    account.amount += expense_instance.count
    form = UpdExpenseForm(request.POST or None, instance=expense_instance)
    if request.method == "POST" and form.is_valid():
        account.amount -= form.cleaned_data['count']
        account.save()
        form.save()
        return redirect("money_keeper_app:account", pk=pk_account)
    return render(request, "money_keeper_app/upd_expense.html", {"form": form})


def delete_expense(request, pk_account, pk_payment):
    expense = Payment.objects.get(pk=pk_payment)
    account = Account.objects.get(pk=pk_account)
    account.amount += expense.count
    account.save()
    expense.delete()
    return redirect("money_keeper_app:account", pk=pk_account)