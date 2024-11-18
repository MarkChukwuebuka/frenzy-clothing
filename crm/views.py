from django.views import View

from products.services.dotd_service import DOTDService, TopShopperService
from products.services.product_service import ProductService
from services.util import CustomRequestUtil


# Create your views here.
class HomeView(View, CustomRequestUtil):
    template_name = "index.html"
    extra_context_data = {
        "title": "Welcome",
    }

    def get(self, request, *args, **kwargs):
        product_service = ProductService(self.request)

        products = product_service.fetch_list()[:10]
        deals = DOTDService(self.request).fetch_active_deals()
        top_shoppers = TopShopperService(self.request).fetch_list()

        self.extra_context_data["products"] = products
        self.extra_context_data["deals"] = deals
        self.extra_context_data["top_shoppers"] = top_shoppers

        return self.process_request(request)


class ContactView(View, CustomRequestUtil):
    template_name = "contact.html"
    extra_context_data = {
        "title": "Contact Us",
    }

    def get(self, request, *args, **kwargs):
        return self.process_request(request)


class AboutView(View, CustomRequestUtil):
    template_name = "about.html"
    extra_context_data = {
        "title": "About Us",
    }

    def get(self, request, *args, **kwargs):
        return self.process_request(request)
