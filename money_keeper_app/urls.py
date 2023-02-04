from django.urls import path
from .views import dashboard, account_page, add_account, delete, upd_account, \
    income_list, add_income, upd_income, delete_income, \
    expense_list, add_expense, upd_expense, delete_expense
# from .views import dashboard

app_name = "money_keeper_app"

urlpatterns = [
    path("delete/<int:pk>", delete, name="delete"),
    path("upd_account/<int:pk>", upd_account, name="upd_account"),
    path("add_account/", add_account, name="add_account"),
    path("account/<int:pk>", account_page, name="account"),
    path("income_list/<int:pk>", income_list, name="income_list"),
    path("add_income/<int:pk>", add_income, name="add_income"),
    path("upd_income/<int:pk_account>/<int:pk_payment>", upd_income, name="upd_income"),
    path("delete_income/<int:pk_account>/<int:pk_payment>", delete_income, name="delete_income"),
    path("expense_list/<int:pk>", expense_list, name="expense_list"),
    path("add_expense/<int:pk>", add_expense, name="add_expense"),
    path("upd_expense/<int:pk_account>/<int:pk_payment>", upd_expense, name="upd_expense"),
    path("delete_expense/<int:pk_account>/<int:pk_payment>", delete_expense, name="delete_expense"),
    path("", dashboard, name="dashboard"),
]
