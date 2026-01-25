from rest_framework import serializers
from subscriptions.models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):

    client_username = serializers.CharField(source='client.username', read_only=True)
    tariff_name = serializers.CharField(source='tariff.tariff_name', read_only=True)
    discount_percent = serializers.CharField(source='tariff.get_discount_percent_display', read_only=True)

    class Meta:
        model = Subscription
        fields = '__all__'