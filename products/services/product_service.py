from django.db import models
from django.db.models import Count, Case, When, ExpressionWrapper, DecimalField, F, Q, Avg

from services.util import CustomRequestUtil


class ProductService(CustomRequestUtil):

    def create_single(self, payload):
        pass

    def fetch_list(self, filter_params=None, category=None):
        q = Q()
        if category:
            q &= Q(categories__name__iexact=category)

        return self.get_base_query().filter(q)


    def get_related_products(self, product_id, limit=5):
        product, _ = self.fetch_single(product_id)

        related_products = self.get_base_query().filter(
            models.Q(categories__in=product.categories.all()) | models.Q(tags__in=product.tags.all())
        ).exclude(id=product.id).distinct()[:limit]

        return related_products

    def get_base_query(self):
        from products.models import Product
        qs = Product.objects.prefetch_related(
            "categories", "tags"
        ).order_by("rating")

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

    def fetch_product_ratings(self, product_id):
        from products.models import ProductReview

        # Aggregate data for average rating and ratings distribution
        ratings_data = ProductReview.objects.filter(product_id=product_id).aggregate(
            avg_rating=Avg('rating'),
            total_reviews=Count('id'),
        )

        # Distribution of ratings (e.g., 5 stars, 4 stars, etc.)
        rating_distribution = ProductReview.objects.filter(product_id=product_id).values(
            'rating'
        ).annotate(
            count=Count('id')
        )

        # Format distribution into a list for progress bar calculations
        total_reviews = ratings_data['total_reviews'] or 1
        rating_distribution = [
            {
                'rating': i,
                'count': next((x['count'] for x in rating_distribution if x['rating'] == i), 0),
                'percentage': (next((x['count'] for x in rating_distribution if x['rating'] == i),
                                    0) / total_reviews) * 100
            }
            for i in range(5, 0, -1)
        ]

        return {
            'avg_rating': round(ratings_data['avg_rating'] or 0, 1),
            'total_reviews': ratings_data['total_reviews'],
            'rating_distribution': rating_distribution,
        }


