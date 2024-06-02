from django.contrib import admin
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "discount_price", "created_at", "updated_at")
    list_filter = ("created_at",)
    search_fields = ("name", "price")



admin.site.register(Product, ProductAdmin)