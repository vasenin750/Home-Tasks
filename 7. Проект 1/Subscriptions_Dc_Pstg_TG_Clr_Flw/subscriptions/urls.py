from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionViewSet, TariffViewSet

router = DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')
router.register(r'tariffs', TariffViewSet, basename='tariff')

urlpatterns = [
    path('', include(router.urls)),
]
