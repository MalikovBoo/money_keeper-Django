from django import forms
from .models import Account


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
