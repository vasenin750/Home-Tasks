from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    telegram_id = models.BigIntegerField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.username