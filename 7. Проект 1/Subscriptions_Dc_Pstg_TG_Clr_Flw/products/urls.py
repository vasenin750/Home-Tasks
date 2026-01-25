from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet
from . import views

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    # ТОЛЬКО HTML интерфейс (префикс orders/)
    path('', views.order_list, name='order_list'),  # /orders/
    path('create/', views.order_create, name='order_create'),  # /orders/create/
    path('<int:pk>/edit/', views.order_update, name='order_update'),  # /orders/1/edit/
    path('<int:pk>/delete/', views.order_delete, name='order_delete'),  # /orders/1/delete/
]