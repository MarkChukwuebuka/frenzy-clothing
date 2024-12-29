from django.contrib import admin

from crm.admin import BaseAdmin
from exchange.models import Transaction, Rate, Coin


@admin.register(Transaction)
class TransactionAdmin(BaseAdmin):
    list_display = ["user", "coin", "amount_in_ngn", "amount_in_usd", "amount_in_crypto", "paid", "status"] + BaseAdmin.list_display
    search_fields = ["coin", "bank_name", "account_name"]
    list_filter = ["status", "paid", "coin"]


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ["buy_rate", "sell_rate"]


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "symbol"]