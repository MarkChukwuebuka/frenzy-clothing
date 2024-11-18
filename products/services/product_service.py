from django.db import models
from django.db.models import Count, Case, When, ExpressionWrapper, DecimalField, F


from services.util import CustomRequestUtil


class ProductService(CustomRequestUtil):

    def create_single(self, payload):
        pass

    def fetch_list(self):
        return self.get_base_query()


    def get_related_products(self, product_id, limit=5):
        product, _ = self.fetch_single(product_id)

        related_products = self.get_base_query().filter(
            models.Q(categories__in=product.categories.all()) | models.Q(tags__in=product.tags.all())
        ).exclude(id=product.id).distinct()[:limit]

        return related_products

    def get_base_query(self):
        from products.models import Product
        qs = Product.available_objects.prefetch_related(
            "categories", "tags"
        ).order_by("rating", "-updated_at")

        qs = qs.annotate(
            discounted_price=Case(
                When(
                    percentage_discount__isnull=False,
                    percentage_discount__gt=0,
                    then=ExpressionWrapper(
                        F('price') - ((F('percentage_discount') * F("price")) / 100),
                        output_field=DecimalField(max_digits=15, decimal_places=2)
                    )
                ),
                default=F('price'),
                output_field=DecimalField(max_digits=15, decimal_places=2)
            ),

            reviews_count=Count('reviews')
        )

        return qs

    def fetch_single(self, product_id):
        product = self.get_base_query().filter(id=product_id).first()
        if not product:
            return None, self.make_error("Product does not exist")

        return product, None

