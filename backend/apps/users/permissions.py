from rest_framework.permissions import BasePermission

from apps.date_selection.models import DateSelectionModel
from bookingApps.utils.permissions_comments_user import PermissionsCommentsUser
from exeptions.jwt_exeption import AuthenticatedCommentApartment, AddDeleteApartmentException
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
        apartmentId = view.kwargs.get('pk')
        exists = DateSelectionModel.objects.filter(user_email=email).filter(apartment_id=apartmentId).exists()
        if not exists:
            raise AuthenticatedCommentApartment
        return bool(request.user)


class CommentOfUserRentedApartment(BasePermission):

    def has_permission(self, request, view):
        emailOwner = request.user
        pk = view.kwargs.get('pk')
        boolApartments = PermissionsCommentsUser.permissions_comments_user(pk, emailOwner)
        if not boolApartments:
            raise AuthenticatedCommentApartment
        return bool(request.user)


class AddDeleteApartment(BasePermission):

    def has_permission(self, request, view):
        email = request.user
        pk = view.kwargs.get('pk')
        userId = UserModel.objects.filter(email=email).values('id')[0].get('id')
        apartment = ApartmentModel.objects.filter(pk=pk).values('user_apartment')[0].get('user_apartment')
        if apartment != userId:
            raise AddDeleteApartmentException
        return bool(request.user)
