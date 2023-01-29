from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100, default='Card')
    amount = models.FloatField()

    def __str__(self):
        return self.user.username + "'s " + self.account_name


class IncomeType(models.Model):
    income_type = models.CharField(max_length=100)

    def __str__(self):
        return self.income_type


class ExpenseType(models.Model):
    expense_type = models.CharField(max_length=100)

    def __str__(self):
        return self.expense_type


class Payment(models.Model):
    account = models.ForeignKey(Account, related_name='payment', on_delete=models.CASCADE)
    count = models.FloatField()
    income = models.ForeignKey(IncomeType, related_name='income', on_delete=models.DO_NOTHING, null=True, blank=True)
    expense = models.ForeignKey(ExpenseType, related_name='expense', on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.income:
            return "+" + str(self.count) + " " + str(self.account) + " " + f"({self.created_at:%Y-%m-%d %H:%M})"
        else:
            return "-" + str(self.count) + " " + str(self.account) + " " + f"({self.created_at:%Y-%m-%d %H:%M})"


# class Expense(models.Model):
#     account = models.ForeignKey(Account, related_name='expense', on_delete=models.CASCADE)
#     expense = models.FloatField()
#     type = models.ForeignKey(ExpenseType, related_name='expense', on_delete=models.DO_NOTHING)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return " -" + str(self.expense) + " " + str(self.account) + " " + str(self.created_at)
