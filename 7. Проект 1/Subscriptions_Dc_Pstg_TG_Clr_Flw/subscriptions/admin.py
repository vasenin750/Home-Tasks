from django.contrib import admin
from users.models import CustomUser
from .models import *
from django.contrib.auth.admin import UserAdmin

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('tariff_name', 'tariff_type', 'display_discount_percent',)
    list_filter = ('tariff_type',)
    search_fields = ('tariff_name', 'tariff_type',)
    ordering = ('tariff_name',)

    def display_discount_percent(self, obj):
        return f"{obj.discount_percent}%"
    display_discount_percent.short_description = 'Скидка'

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('get_client_username', 'get_tariff_name', 'price', 'get_discount_percent',)
    list_filter = ('tariff',)
    search_fields = ('client__username', 'tariff__tariff_name',)
    ordering = ('-start_date',)

    def get_client_username(self, obj):
        return obj.client.username
    get_client_username.short_description = 'Клиент'
    get_client_username.admin_order_field = 'client__username'

    def get_tariff_name(self, obj):
        return obj.tariff.tariff_name
    get_tariff_name.short_description = 'Тариф'
    get_tariff_name.admin_order_field = 'tariff__tariff_name'

    def get_discount_percent(self, obj):
        return obj.tariff.discount_percent_str

    get_discount_percent.short_description = 'Скидка тарифа'