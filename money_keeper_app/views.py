from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import Payment, Account


# def dashboard(request):
#     return render(request, "base.html")
def dashboard(request):
    if request.user.is_authenticated:
        accounts = Account.objects.filter(user=request.user)
        if len(accounts) > 0:
            return render(request, "money_keeper_app/accounts_list.html", {"accounts": accounts})
        else:
            # если у пользователя нет счетов
            return render(request, "base.html")
    else:
        # если неавторизован
        return render(request, "base.html")


def account_page(request, pk):
    if request.user.is_authenticated:
        account = Account.objects.get(pk=pk)
        payments = Payment.objects.filter(account=account.id)
        return render(request, "money_keeper_app/account.html", {"account": account, "payments": payments})
    else:
        # если неавторизован
        return render(request, "base.html")


def add_account(request):
    if request.user.is_authenticated:
        form = AccountForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                account = form.save(commit=False)
                account.user = request.user
                account.save()
                return redirect("money_keeper_app:dashboard")
        return render(request, "money_keeper_app/add_account.html", {"form": form})

    else:
        # если неавторизован
        return render(request, "base.html")


def income_list(request, pk):
    if request.user.is_authenticated:
        account = Account.objects.get(pk=pk)
        incomes = Payment.objects.filter(account=account.id, expense=None)
        return render(request, "money_keeper_app/income_list.html", {"account": account, "incomes": incomes})
    else:
        # если неавторизован
        return render(request, "base.html")


def expense_list(request, pk):
    if request.user.is_authenticated:
        account = Account.objects.get(pk=pk)
        expenses = Payment.objects.filter(account=account.id, income=None)
        return render(request, "money_keeper_app/expense_list.html", {"account": account, "expenses": expenses})
    else:
        # если неавторизован
        return render(request, "base.html")
