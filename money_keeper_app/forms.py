from django import forms
from .models import Account, Payment, IncomeType, ExpenseType


class NewAccountForm(forms.ModelForm):

    account_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Enter the name",
                "class": "input is-success is-normal",
            }
        ),
    )
    amount = forms.FloatField(
        required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                "class": "input is-success is-normal",
            }
        ),
    )

    class Meta:
        model = Account
        exclude = ("user",)


class UpdAccountForm(forms.ModelForm):

    account_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Enter the name",
                "class": "input is-success is-normal",
            }
        ),
    )

    class Meta:
        model = Account
        fields = ["account_name"]


class NewIncomeForm(forms.ModelForm):

    choices_list = [(obj.id, str(obj)) for obj in IncomeType.objects.all()]

    count = forms.FloatField(
        required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                "class": " input is-info control ",
            }
        ),
    )

    income_type = forms.ChoiceField(
        required=True,
        widget=forms.widgets.Select(
            attrs={
                "class": " input is-info ",
            }
        ),
        choices=choices_list
    )

    class Meta:
        model = Payment
        fields = ["count"]


class UpdIncomeForm(forms.ModelForm):

    choices_list = [(obj.id, str(obj)) for obj in IncomeType.objects.all()]

    count = forms.FloatField(
        required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                "class": " input is-info control ",
            }
        ),
    )

    income_type = forms.ChoiceField(
        required=True,
        widget=forms.widgets.Select(
            attrs={
                "class": " input is-info ",
            }
        ),
        choices=choices_list
    )

    class Meta:
        model = Payment
        fields = ["count"]


class NewExpenseForm(forms.ModelForm):

    choices_list = [(obj.id, str(obj)) for obj in ExpenseType.objects.all()]

    count = forms.FloatField(
        required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                "class": " input is-info control ",
            }
        ),
    )

    expense_type = forms.ChoiceField(
        required=True,
        widget=forms.widgets.Select(
            attrs={
                "class": " input is-info ",
            }
        ),
        choices=choices_list
    )

    class Meta:
        model = Payment
        fields = ["count"]


class UpdExpenseForm(forms.ModelForm):

    choices_list = [(obj.id, str(obj)) for obj in ExpenseType.objects.all()]

    count = forms.FloatField(
        required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                "class": " input is-info control ",
            }
        ),
    )

    expense_type = forms.ChoiceField(
        required=True,
        widget=forms.widgets.Select(
            attrs={
                "class": " input is-info ",
            }
        ),
        choices=choices_list
    )

    class Meta:
        model = Payment
        fields = ["count"]
