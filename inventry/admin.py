from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "in_stock", "updated_at")
    list_filter = ("in_stock",)
    search_fields = ("name",)
    ordering = ("name",)
    list_editable = ("price", "quantity", "in_stock")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("name",)}),
        ("Stock", {"fields": ("price", "quantity", "in_stock")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )