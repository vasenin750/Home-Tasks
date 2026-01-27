from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from config.permissions import IsOwnerOrSuperuser
from subscriptions.models import Tariff, Subscription
from subscriptions.serializers import TariffSerializer, SubscriptionSerializer

class TariffViewSet(ModelViewSet):

    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]

class SubscriptionViewSet(ModelViewSet):

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Subscription.objects.all()
        return Subscription.objects.filter(client=user)