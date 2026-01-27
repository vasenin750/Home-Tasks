from rest_framework import permissions

class IsOwnerOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if hasattr(obj, 'client'):
            return obj.client == request.user

        if hasattr(obj, 'user'):
            return obj.user == request.user

        return False