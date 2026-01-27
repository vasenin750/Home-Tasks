from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from config import settings

class Tariff(models.Model):
    tariff_name = models.CharField(max_length=50)
    TARIFF_TYPES = (('full', 'Full'), ('student', 'Student'), ('discount', 'Discount'))
    tariff_type = models.CharField(max_length=10, choices=TARIFF_TYPES)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    @property
    def discount_percent_str(self):
        return f"{self.discount_percent}%"

    def __str__(self):
        return f'{self.tariff_name}, {self.tariff_type}'

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

class Subscription(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_subscriptions', on_delete=models.PROTECT)
    tariff = models.ForeignKey(Tariff, related_name='tariff_subscriptions', on_delete=models.PROTECT)
    price = models.PositiveIntegerField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def get_client_username(self):
        return self.client.username
    get_client_username.short_description = 'Клиент'

    def get_tariff_name(self):
        return self.tariff.tariff_name
    get_tariff_name.short_description = 'Тариф'

    def __str__(self):
        return f'{self.client.username}, {self.tariff.tariff_name}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ['-start_date']