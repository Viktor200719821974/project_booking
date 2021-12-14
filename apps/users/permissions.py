from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission

from apps.date_selection.models import DateSelectionModel
from exeptions.jwt_exeption import AuthenticatedCommentApartment, AuthenticatedCommentUser
from apps.apartments.models import ApartmentModel
from apps.users.models import UserModel


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

# class AddDeleteApartment(BasePermission):
#
#     def has_permission(self, request, view, **kwargs):
#         email = request.user
#         pk = request.
#         address = get_object_or_404(ApartmentModel, pk=pk)
#         print(pk)
#         print(type(request))
#         userId = UserModel.objects.filter(email=email).values('id')[0].get('id')
#         print(userId)
#         exists = ApartmentModel.objects.filter(user_apartment=userId).exists()
#         if not exists:
#             raise AuthenticatedCommentUser
#         return bool(request.user)