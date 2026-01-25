"""
URL configuration for Subscriptions_Dc_Pstg_TG_Clr_Flw project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from subscriptions.views import SubscriptionView
from products.views import ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'subscriptions', SubscriptionView, basename='subscription')
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Все API: /api/subscriptions/, /api/products/, /api/orders/
    path('orders/', include('products.urls')),  # HTML: /orders/, /orders/create/ и т.д.
]