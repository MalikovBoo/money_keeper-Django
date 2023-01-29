from django.shortcuts import render
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


def income_list(request):
    account = Account.objects.filter(user=request.user)[0]
    incomes = Payment.objects.filter(account=account)
    return render(request, "money_keeper_app/income_list.html", {"incomes": incomes})


def expense_list(request):
    account = Account.objects.filter(user=request.user)[0]
    expenses = Payment.objects.filter(account=account)
    return render(request, "money_keeper_app/expense_list.html", {"expenses": expenses})
