from rest_framework import permissions
from rest_framework.request import Request

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user