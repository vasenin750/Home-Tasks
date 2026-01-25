from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class SubscriptionCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        path = request.path_info

        if path.startswith('/orders/') or path.startswith('/api/orders/'):

            if not request.user.is_authenticated:
                return JsonResponse(
                    {'Ошибка': 'Нужна аутентификация пользователя'},
                    json_dumps_params={'ensure_ascii': False},
                    status=401
                )

            from subscriptions.models import Subscription

            has_active_subscription = Subscription.objects.filter(client=request.user, is_active=True).exists()

            if not has_active_subscription:
                return JsonResponse(
                    {'Ошибка': 'У вас нет активной подписки'},
                    json_dumps_params={'ensure_ascii': False},
                    status=403
                )

        return None