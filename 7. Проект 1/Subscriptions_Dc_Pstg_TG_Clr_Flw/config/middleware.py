import logging
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('django')

class SubscriptionCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        logger.debug("Начало работы SubscriptionCheckMiddleware")

        path = request.path_info

        if path.startswith('/static/') or path.startswith('/media/'):
            return None

        logger.debug(f"Authenticated user: {request.user}")
        logger.debug(f"Request path: {path}")
        logger.debug(f"User authenticated: {request.user.is_authenticated}")

        if path.startswith('/api/orders/'):

            if not request.user.is_authenticated:
                logger.debug("User is not authenticated")
                return JsonResponse(
                    {'Ошибка': 'Нужна аутентификация пользователя'},
                    json_dumps_params={'ensure_ascii': False},
                    status=401
                )

            user = request.user
            if hasattr(user, 'user_subscriptions'):
                has_active_subscription = user.user_subscriptions.filter(is_active=True).exists()
            else:
                has_active_subscription = False

            if not has_active_subscription:
                logger.debug("User does not have an active subscription")
                return JsonResponse(
                    {'Ошибка': 'У вас нет активной подписки'},
                    json_dumps_params={'ensure_ascii': False},
                    status=403
                )

        return None