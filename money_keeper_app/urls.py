from django.urls import path
from .views import dashboard, income_list, add_income, expense_list, add_expense, \
    account_page, add_account, delete, upd_account
# from .views import dashboard

app_name = "money_keeper_app"

urlpatterns = [
    path("delete/<int:pk>", delete, name="delete"),
    path("upd_account/<int:pk>", upd_account, name="upd_account"),
    path("add_account/", add_account, name="add_account"),
    path("account/<int:pk>", account_page, name="account"),
    path("income_list/<int:pk>", income_list, name="income_list"),
    path("add_income/<int:pk>", add_income, name="add_income"),
    path("expense_list/<int:pk>", expense_list, name="expense_list"),
    path("add_expense/<int:pk>", add_expense, name="add_expense"),
    path("", dashboard, name="dashboard"),
]
