from django.contrib import admin

from accounts.models import User, Role
from crm.admin import BaseAdmin


# Register your models here.

@admin.register(Role)
class RoleAdmin(BaseAdmin):
    list_display = ["name"] + BaseAdmin.list_display
    search_fields = ["name"]


@admin.register(User)
class UserAdmin(BaseAdmin):
    list_display = ["email", "first_name", "last_name"] + BaseAdmin.list_display
    search_fields = ["email", "first_name", "last_name"]
    readonly_fields = ["password"]
    list_filter = ["user_type"]
    autocomplete_fields = ["roles"]

