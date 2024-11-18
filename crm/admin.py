from django.contrib import admin

from crm.models import Color


class BaseAdmin(admin.ModelAdmin):
    list_display = ["created_by", "created_at", "updated_at", "deleted_at"]
    readonly_fields = ["updated_by", "deleted_by", "deactivated_by", "deactivated_by"]
    autocomplete_fields = ["created_by", "updated_by", "deactivated_by", "deleted_by"]
    list_filter = []
    date_hierarchy = "created_at"


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'hex_code']
    list_filter = ['name', 'hex_code']
    search_fields = ['name', 'hex_code']