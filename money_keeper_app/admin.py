from django.contrib import admin
from django.contrib.auth.models import Group
from .models import ExpenseType, IncomeType, Payment, Account

# Register your models here.
admin.site.unregister(Group)
admin.site.register(Account)
admin.site.register(ExpenseType)
admin.site.register(IncomeType)
admin.site.register(Payment)
