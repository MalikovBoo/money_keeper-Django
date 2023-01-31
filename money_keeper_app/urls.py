from django.urls import path
from .views import dashboard, income_list, expense_list, account_page, add_account
# from .views import dashboard

app_name = "money_keeper_app"

urlpatterns = [
    path("add_account/", add_account, name="add_account"),
    path("account/<int:pk>", account_page, name="account"),
    path("income_list/<int:pk>", income_list, name="income_list"),
    path("expense_list/<int:pk>", expense_list, name="expense_list"),
    path("", dashboard, name="dashboard"),
]
