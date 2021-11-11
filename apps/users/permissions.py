from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)