from rest_framework.viewsets import ModelViewSet
from subscriptions.models import Subscription #Product
from subscriptions.serializers import SubscriptionSerializer #ProductsSerializer

class SubscriptionView(ModelViewSet):

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer