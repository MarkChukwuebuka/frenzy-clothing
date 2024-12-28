from django.urls import path
from . import views
from payments.views import start_order, CreateListOrderView, RetrieveUpdateDeleteOrderView
from .views import ExchangeView, BuyView, SellView

urlpatterns = [
    path('', ExchangeView.as_view(), name='exchange'),
    path('buy/', BuyView.as_view(), name='buy'),
    path('sell/', SellView.as_view(), name='sell'),


]
