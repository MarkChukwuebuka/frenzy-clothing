
from cloudinary.models import CloudinaryField
from django.db import models
from django.utils import timezone

from accounts.models import User
from crm.models import BaseModel, Color
from products.views import generate_sku


class Availability(models.TextChoices):
    in_stock = "In Stock"
    out_of_stock = "Out of Stock"


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Tag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    percentage_discount = models.IntegerField(null=True, blank=True)
    sku = models.CharField(max_length=255, default=generate_sku, unique=True)
    categories = models.ManyToManyField(Category, blank=True, related_name="product_tags")
    tags = models.ManyToManyField(Tag, blank=True, related_name="product_categories")
    description = models.TextField(null=True, blank=True)
    availability = models.CharField(max_length=255, choices=Availability.choices, db_default=Availability.in_stock)
    rating = models.IntegerField(null=True, blank=True)

    cover_image = CloudinaryField('cover image', blank=True, null=True)
    image1 = CloudinaryField('image1', blank=True, null=True)
    image2 = CloudinaryField('image2', blank=True, null=True)
    image3 = CloudinaryField('image3', blank=True, null=True)
    image4 = CloudinaryField('image4', blank=True, null=True)
    image5 = CloudinaryField('image5', blank=True, null=True)
    image6 = CloudinaryField('image6', blank=True, null=True)

    colors = models.ManyToManyField(Color, blank=True, related_name="product_colors")

    def __str__(self):
        return self.name


class ProductReview(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_reviews")
    rating = models.IntegerField(null=True, blank=True)
    review = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name}'s Review on {self.product}"


class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlisted_by")

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.first_name} - {self.product.name}"



class DealOfTheDay(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    number_of_available_stock = models.IntegerField(default=0)

    def __str__(self):
        return f"Deal for {self.product.name} - {self.discount_percentage}% off"


class TopShopper(BaseModel):
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, default="Customer")
    review = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.full_name
