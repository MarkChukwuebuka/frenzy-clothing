from cloudinary.models import CloudinaryField
from django.db import models

from crm.models import BaseModel
from exchange.services.transaction_service import generate_trxn_ref


class StatusChoices(models.TextChoices):
    pending = 'Pending'
    completed = 'Completed'
    declined = 'Declined'

class TransTypeChoices(models.TextChoices):
    buy = 'Buy'
    sell = 'Sell'


# Create your models here.
class Coin(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    qr_code = CloudinaryField('qr_code')

    def __str__(self):
        return self.name


class Transaction(BaseModel):
    coin = models.CharField(max_length=255)
    wallet_address = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=StatusChoices.choices, default=StatusChoices.pending)
    trans_type = models.CharField(max_length=25, choices=TransTypeChoices.choices, default=TransTypeChoices.buy)
    paid = models.BooleanField(default=False)
    rate = models.FloatField(null=True, blank=True)
    amount_in_ngn = models.FloatField(null=True, blank=True)
    amount_in_usd = models.FloatField(null=True, blank=True)
    amount_in_crypto = models.FloatField(null=True, blank=True)
    ref = models.CharField(max_length=255, default=generate_trxn_ref)
    user = models.ForeignKey("accounts.User", related_name="transactions", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Rate(models.Model):
    buy_rate = models.FloatField(default=0.0)
    sell_rate = models.FloatField(default=0.0)