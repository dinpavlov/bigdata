from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение на PUT и DELETE для создателя задачи
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.assigner == request.user
