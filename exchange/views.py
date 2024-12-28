from django.views import View

from exchange.models import Rate
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


        return self.process_request(request)


class SellView(View, CustomRequestUtil):
    template_name = "sell.html"
    template_on_error = "sell.html"
    extra_context_data = {
        "title": "Sell Crypto",
    }

    def get(self, request, *args, **kwargs):
        self.extra_context_data['sell_rate'] = Rate.objects.first().sell_rate
        self.extra_context_data['bank'] = BankAccount.objects.first()

        return self.process_request(request)