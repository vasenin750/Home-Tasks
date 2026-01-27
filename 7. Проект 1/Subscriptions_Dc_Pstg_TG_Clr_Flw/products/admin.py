from django.contrib import admin
from products.models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total_price', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username', 'product__name',)