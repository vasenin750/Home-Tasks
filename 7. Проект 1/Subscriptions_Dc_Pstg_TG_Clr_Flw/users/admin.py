from django.contrib import admin
from users.models import CustomUser
from .models import *
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('phone',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {'fields': ('phone',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
