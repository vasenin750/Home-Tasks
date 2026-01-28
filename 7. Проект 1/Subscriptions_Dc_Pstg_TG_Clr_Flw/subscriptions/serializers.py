from rest_framework import serializers
from django.contrib.auth import get_user_model
from subscriptions.models import Tariff, Subscription

User = get_user_model()

class TariffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tariff
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):

    client_username = serializers.CharField(source='client.username', read_only=True)
    tariff_name = serializers.CharField(source='tariff.tariff_name', read_only=True)
    discount_percent = serializers.CharField(source='tariff.discount_percent_str', read_only=True)

    client = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False
    )

    tariff = serializers.PrimaryKeyRelatedField(
        queryset=Tariff.objects.all()
    )

    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ('start_date',)