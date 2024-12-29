from django.views import View

from exchange.models import Rate, Coin
from exchange.services.transaction_service import TransactionService
from payments.models import BankAccount
from services.util import CustomRequestUtil


class ExchangeView(View, CustomRequestUtil):
    template_name = "exchange.html"
    extra_context_data = {
        "title": "Exchange",
    }

    def get(self, request, *args, **kwargs):

        return self.process_request(request)


class BuyView(View, CustomRequestUtil):
    template_name = "buy.html"
    template_on_error = "buy.html"
    extra_context_data = {
        "title": "Buy Crypto",
    }

    def get(self, request, *args, **kwargs):
        self.extra_context_data['buy_rate'] = Rate.objects.first().buy_rate
        self.extra_context_data['bank'] = BankAccount.objects.first()
        self.extra_context_data['coins'] = Coin.objects.all()


        return self.process_request(request)

    def post(self, request, *args, **kwargs):
        self.template_name = None
        self.extra_context_data = {
            "title": "Transactions",
        }

        payload = {
            "coin": request.POST.get('coin'),
            "wallet_address": request.POST.get('wallet-address'),
            "rate": request.POST.get('rate'),
            "amount_in_ngn": request.POST.get('amount-in-ngn'),
            "amount_in_usd": request.POST.get('amount-in-usd'),
            "amount_in_crypto": request.POST.get('amount-in-crypto'),
            "bank_name": request.POST.get('bank-name'),
            "account_name": request.POST.get('account-name'),
            "account_number": request.POST.get('account-number'),
            "trans_type": "Buy"

        }

        trxn_service = TransactionService(self.request)

        return self.process_request(
            request, target_function=trxn_service.create_single,
            target_view="transactions", payload=payload
        )


class SellView(View, CustomRequestUtil):
    template_name = "sell.html"
    template_on_error = "sell.html"
    extra_context_data = {
        "title": "Sell Crypto",
    }

    def get(self, request, *args, **kwargs):
        self.extra_context_data['sell_rate'] = Rate.objects.first().sell_rate
        self.extra_context_data['bank'] = BankAccount.objects.first()
        self.extra_context_data['coins'] = Coin.objects.all()

        return self.process_request(request)

    def post(self, request, *args, **kwargs):

        self.extra_context_data = {
            "title": "Transactions",
        }

        payload = {
            "coin": request.POST.get('coin'),
            "wallet_address": request.POST.get('wallet-address'),
            "rate": request.POST.get('rate'),
            "amount_in_ngn": request.POST.get('amount-in-ngn'),
            "amount_in_usd": request.POST.get('amount-in-usd'),
            "amount_in_crypto": request.POST.get('amount-in-crypto'),
            "bank_name": request.POST.get('bank-name'),
            "account_name": request.POST.get('account-name'),
            "account_number": request.POST.get('account-number'),
            "trans_type": "Sell"
        }

        trxn_service = TransactionService(self.request)

        return self.process_request(
            request, target_function=trxn_service.create_single,
            target_view="transactions", payload=payload
        )



class TransactionView(View, CustomRequestUtil):
    template_name = "transactions.html"
    context_object_name = "transactions"

    extra_context_data = {
        "title": "Transactions",
    }

    def get(self, request, *args, **kwargs):
        trxn_service = TransactionService(self.request)

        return self.process_request(request, target_function=trxn_service.fetch_list)