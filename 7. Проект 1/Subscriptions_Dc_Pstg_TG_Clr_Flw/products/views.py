from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from config.permissions import IsOwnerOrSuperuser
from products.models import Product, Order
from products.serializers import ProductSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)