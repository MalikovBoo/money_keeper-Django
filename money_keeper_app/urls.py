from django.urls import path
from .views import dashboard, income_list, expense_list, account_page
# from .views import dashboard

app_name = "money_keeper_app"

urlpatterns = [
    path("account/<int:pk>", account_page, name="account"),
    path("income_list/", income_list, name="income_list"),
    path("expense_list/", expense_list, name="expense_list"),
    path("", dashboard, name="dashboard"),
]
