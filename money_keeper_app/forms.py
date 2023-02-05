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


class NewIncomeTypeForm(forms.ModelForm):

    income_type = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Enter the type",
                "class": "input is-success is-normal",
            }
        ),
    )

    class Meta:
        model = IncomeType
        fields = ['income_type']


class UpdIncomeTypeForm(forms.ModelForm):

    income_type = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Enter the type",
                "class": "input is-success is-normal",
            }
        ),
    )

    class Meta:
        model = IncomeType
        fields = ['income_type']


class NewIncomeForm(forms.ModelForm):

    count = forms.FloatField(
        required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                "class": " input is-info control ",
            }
        ),
    )

    income_type = forms.ModelChoiceField(
        required=True,
        widget=forms.widgets.Select(
            attrs={
                "class": " input is-info ",
            }
        ),
        queryset=IncomeType.objects.all()
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
        choices=[(obj.id, str(obj)) for obj in IncomeType.objects.all()]
    )

    class Meta:
        model = Payment
        fields = ["count"]


class NewExpenseTypeForm(forms.ModelForm):

    expense_type = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Enter the type",
                "class": "input is-success is-normal",
            }
        ),
    )

    class Meta:
        model = ExpenseType
        fields = ['expense_type']


class UpdExpenseTypeForm(forms.ModelForm):
    expense_type = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Enter the type",
                "class": "input is-success is-normal",
            }
        ),
    )

    class Meta:
        model = ExpenseType
        fields = ['expense_type']


class NewExpenseForm(forms.ModelForm):

    count = forms.FloatField(
        required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                "class": " input is-info control ",
            }
        ),
    )

    expense_type = forms.ModelChoiceField(
        required=True,
        widget=forms.widgets.Select(
            attrs={
                "class": " input is-info ",
            }
        ),
        queryset=ExpenseType.objects.all()
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
        choices=[(obj.id, str(obj)) for obj in ExpenseType.objects.all()]
    )

    class Meta:
        model = Payment
        fields = ["count"]
