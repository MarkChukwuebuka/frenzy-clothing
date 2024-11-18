from django.db import models
from django.db.models.signals import post_save

from accounts.models import User
from crm.models import BaseModel
from products.models import Product
import secrets


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
    total_cost = models.IntegerField(default=0)
    status = models.CharField(max_length=25, choices=StatusChoices.choices, default=StatusChoices.ordered)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.user}'

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_order = Order.objects.get(pk=self.pk)
            # Check if the status has changed to "shipped"
            if old_order.status != self.status and self.status == StatusChoices.shipped:
                #TODO: send mail to notify customer
                pass
                # print("shipped")

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

    def __str__(self):
        return f"{self.user} - {self.amount}"

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(10)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    def amount_value(self):
        return int(self.amount) * 100

