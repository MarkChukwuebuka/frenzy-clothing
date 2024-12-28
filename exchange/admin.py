from django.contrib import admin

from crm.admin import BaseAdmin
from exchange.models import Transaction


# Register your models here.

@admin.register(Transaction)
class TransactionAdmin(BaseAdmin):
    list_display = ["user", "coin", "amount", "paid", "status"] + BaseAdmin.list_display
    search_fields = ["coin", "bank_name", "account_name"]
    list_filter = ["status", "paid", "coin"]
