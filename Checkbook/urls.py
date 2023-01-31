from django.urls import path
from . import views


urlpatterns = [
    # sets the url path to home page index.html
    path('', views.home, name='index'),
    # sets the url for creating a new account to CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    # sets the url path for a balance sheet to BalanceSheet.html
    path('<int:pk>/balance/', views.balance, name='balance'),
    # sets the url path to add new transactions to AddNewtransactions.html
    path('transaction/', views.transaction, name='transaction')
]