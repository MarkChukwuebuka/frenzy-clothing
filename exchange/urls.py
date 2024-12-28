from django.urls import path
from .views import ExchangeView, BuyView, SellView

urlpatterns = [
    path('', ExchangeView.as_view(), name='exchange'),
    path('buy/', BuyView.as_view(), name='buy'),
    path('sell/', SellView.as_view(), name='sell'),
    path('transactions/', TransactionView.as_view(), name='transactions'),


]
