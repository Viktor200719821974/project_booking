from rest_framework.permissions import BasePermission

from apps.date_selection.models import DateSelectionModel
from exeptions.jwt_exeption import AuthenticatedCommentApartment, AuthenticatedCommentUser


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class CommentRentedApartment(BasePermission):
    def has_permission(self, request, view):
        email = request.user
        exists = DateSelectionModel.objects.filter(user_email=email).exists()
        if not exists:
            raise AuthenticatedCommentApartment
        return bool(request.user)


class CommentOfUserRentedApartment(BasePermission):

    def has_permission(self, request, view):
        email = request.user
        exists = DateSelectionModel.objects.filter(user_email=email).exists()
        if not exists:
            raise AuthenticatedCommentUser
        return bool(request.user)