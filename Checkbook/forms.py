from django.forms import ModelForm
from .models import Account, Transaction


# Creates the account form based on the account model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# creates the transaction form based on the transaction model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'