from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models import TextChoices, Q
from django.db.models.signals import post_save

from crm.models import BaseModel


class UserTypes(TextChoices):
    admin = "Admin"
    customer = "Customer"


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.user_type = UserTypes.admin
        user.save(using=self._db)
        return user




class User(AbstractBaseUser, BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=70, null=True, blank=True)
    image_url = models.URLField(null=True)
    user_type = models.CharField(
        max_length=255, default=UserTypes.customer, choices=UserTypes.choices
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    date_joined = None

    roles = models.ManyToManyField(
        "Role", related_query_name="roles", blank=True
    )

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True  # Can be more specific based on user permissions

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True

    groups = None
    user_permissions = None

    def get_short_name(self):
        return self.get_full_name()

    def get_full_name(self):
        return " ".join(
            [
                self.first_name or "",
                self.last_name or "",
            ]
        ).replace("\s+", " ").strip()

    def has_permission(self, perm_name):
        if self.is_superuser:
            return True

        q = Q(permissions__name=perm_name)

        return self.roles.filter(q).exists()

    def __str__(self):
        return self.get_full_name() + f" ({self.email})"


class Permission(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    group_name = models.CharField(max_length=255)


class Role(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    permissions = models.ManyToManyField(Permission, related_name="roles")


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.email


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)
