from lib2to3.fixes.fix_input import context

from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.signals import post_save

from accounts.models import User
from crm.models import BaseModel
from products.models import Product
import secrets

from services.util import send_email


class StatusChoices(models.TextChoices):
    ordered = 'Ordered'
    shipped = 'Shipped'
    delivered = 'Delivered'


class Order(BaseModel):

    user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, default="")
    last_name = models.CharField(max_length=250, default="")
    address = models.CharField(max_length=250, default="")
    email = models.EmailField(max_length=250, default="")
    state = models.CharField(max_length=250, default="")
    lga = models.CharField(max_length=250, default="")
    phone = models.CharField(max_length=250, default="")
    paid = models.BooleanField(default=False)
    total_cost = models.FloatField(default=0.0)
    status = models.CharField(max_length=25, choices=StatusChoices.choices, default=StatusChoices.ordered)
    ref = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.user}'

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_order = Order.objects.get(pk=self.pk)
            # Check if the status has changed to "shipped"
            context = {
                'name': self.first_name,
                'ref': self.ref,
                'amount': self.total_cost
            }
            if old_order.status != self.status and self.status == StatusChoices.shipped:
                send_email('emails/order-shipped.html', context, 'Order Shipped', self.email)

        super().save(*args, **kwargs)



class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.order} - {self.product}'



class Payment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='payment')
    receipt = CloudinaryField('receipt', blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.amount}"

    def save(self, *args, **kwargs):
        # Check if the payment already exists
        if self.pk is not None:
            old_payment = Payment.objects.get(pk=self.pk)

            # Check if the `verified` status has changed
            if old_payment.verified != self.verified:
                if self.order:
                    # Update the `paid` field of the associated order
                    self.order.paid = self.verified
                    self.order.save()

                # Send email notification if `verified` is changed to True
                if self.verified:
                    context = {
                        'name': self.order.first_name,
                        'ref' : self.ref,
                        'amount' : self.amount
                    }
                    send_email('emails/payment-verified.html', context, 'Payment Verified', self.email)

        super().save(*args, **kwargs)



class BankAccount(models.Model):
    bank_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)

    def __str__(self):
        return self.bank_name