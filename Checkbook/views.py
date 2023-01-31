from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# Create your views here.
# this function will render the homepage when requested
def home(request):
    form = TransactionForm(data=request.POST or None)  # Gets the transaction form
    #  Checks if the request method is POST
    if request.method == 'POST':
        pk = request.POST['account']  # if the form is submitted, retrieve the account the user wants to view
        return balance(request, pk)  # call the balance function to render the balance sheet
    content = {'form': form}
    # adds content to the form page
    return render(request, 'checkbook/index.html', content)

# this function will render the create account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None) # get the account form
    # checks if the request is POST
    if request.method == 'POST':
        if form.is_valid():  # checks if the form is valid, and if so saves the form
            form.save()  # saves new account
            return redirect('index')  # sends user back to the homepage
    content = {'form': form}  # saves content to the template as a dictionary
    # adds content of the form to the page
    return render(request, 'checkbook/CreateNewAccount.html', content)

def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # get the requested account using the pk
    transactions = Transaction.Transactions.filter(account=pk)  # get all the accounts transactions
    current_total = account.initial_deposit  # create account total variable starting with initial deposit value
    table_contents = {}  # creates a dictionary for transaction information
    for t in transactions:  # loop through to sort deposits from withdrawals
        if t.type == 'Deposit':
            current_total += t.amount  # if deposit, add to the current balance
            table_contents.update({t: current_total})  # add transaction and total to the dictionary
        else:
            current_total -= t.amount  # if withdrawal, subtract from the current balance
            table_contents.update({t: current_total})  # add transaction and total to the dictionary
        # Pass account, account total balance, and transaction info to the template
        content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# this function will render the transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None) # get the transaction form
    # checks if the request is POST
    if request.method == 'POST':
        if form.is_valid():  # checks if the form is valid, and if so saves the form
            pk = request.POST['account']  # get the account the transaction was for
            form.save()  # saves new account
            return balance(request, pk)  # renders the updated account balance sheet
    content = {'form': form}
    # adds content of the form to the page
    return render(request, 'checkbook/AddTransaction.html', content)


