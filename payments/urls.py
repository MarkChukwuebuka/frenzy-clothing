from django.urls import path
from . import views
from payments.views import verify_payment, start_order, CreateListOrderView, RetrieveUpdateDeleteOrderView

urlpatterns = [
    path('order/', start_order, name='start_order'),
    path('my-orders/', CreateListOrderView.as_view(), name='my-orders'),
    path('order/<int:order_id>/', RetrieveUpdateDeleteOrderView.as_view(), name='order-detail'),

    path('verify_payment<str:ref>/', verify_payment, name='verify_payment')

]
