from django.contrib.auth import get_user_model
from rest_framework import serializers
from products.models import Product, Order

User = get_user_model()

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'created_at']

class OrderSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source='product.name', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )

    class Meta:
        model = Order
        fields = ['id', 'user', 'username', 'product', 'product_name', 'quantity', 'total_price', 'created_at', 'updated_at']