import random
import string

from django.http import JsonResponse
from django.views import View

from products.services.product_service import ProductService
from products.services.review_service import ProductReviewService
from products.services.wishlist_service import WishlistService
from services.util import CustomRequestUtil


class RetrieveUpdateDeleteProductView(View, CustomRequestUtil):
    template_name = "product-detail.html"
    context_object_name = 'product'
    template_on_error = "product-detail.html"

    def get(self, request, *args, **kwargs):
        product_service = ProductService(self.request)
        product, error = product_service.fetch_single(kwargs.get("product_id"))

        related_products = product_service.get_related_products(product.id)

        self.extra_context_data = {
            "title": product.name,
            "related_products": related_products
        }

        return self.process_request(
            request, target_function=product_service.fetch_single, product_id=kwargs.get("product_id")
        )

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        rating = request.POST.get('rating')
        review = request.POST.get('review')

        product_service = ProductService(self.request)
        product, error = product_service.fetch_single(product_id)

        self.extra_context_data = {
            "title": product.name,
            'product':product
        }

        payload = {
            "rating": rating,
            "review": review,
            "product": product,
        }

        product_review_service = ProductReviewService(self.request)

        return self.process_request(
            request, target_function=product_review_service.create_single,
            target_view="product-detail", payload=payload
        )


class CreateListProductView(View, CustomRequestUtil):
    extra_context_data = {
        "title": "Luxe Shop"
    }

    def get(self, request, *args, **kwargs):
        self.template_name = "shop.html"
        self.context_object_name = 'products'

        category = kwargs.get('name', None)

        product_service = ProductService(self.request)

        return self.process_request(
            request, target_function=product_service.fetch_list, category=category
        )

class AddOrRemoveFromWishlistView(View, CustomRequestUtil):
    def post(self, request, *args, **kwargs):
        product_id = int(request.POST.get('product_id'))
        wishlist_service = WishlistService(self.request)

        message, error = wishlist_service.add_or_remove({"product": product_id})

        if error:
            return JsonResponse({"error": error}, status=400)

        return JsonResponse({"message": message})


class WishlistView(View, CustomRequestUtil):
    extra_context_data = {
        "title":"My Wishlist"
    }
    def get(self, request, *args, **kwargs):
        self.template_name = "wishlist.html"
        self.context_object_name = 'wishlist_items'

        wishlist_service = WishlistService(self.request)

        return self.process_request(
            request, target_function=wishlist_service.fetch_list
        )

def generate_sku(product_name):
    name_part = product_name[:3].upper()

    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    sku = f"{name_part}-{random_part}"

    return sku