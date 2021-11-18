from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .serializers import UserModelSerializer
from .permissions import IsSuperUser, IsManagerUser

UserModel: User = get_user_model()


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_id='List of users', operation_summary='Get all users'))
@method_decorator(name='post',
                  decorator=swagger_auto_schema(operation_id='Create user',
                                                operation_summary='Create user'))
class UsersListCreateView(ListCreateAPIView):
    """
    get:
         Get all users
     post:
         Create user
    """
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return AllowAny(),
        return IsAdminUser(),

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def get_serializer_context(self):
        return {'request': self.request}


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_id='Get of user', operation_summary='Get user'))
@method_decorator(name='put',
                  decorator=swagger_auto_schema(operation_id='All update of user', operation_summary='All update'))
@method_decorator(name='patch',
                  decorator=swagger_auto_schema(operation_id='Update user', operation_summary='Update user'))
@method_decorator(name='delete',
                  decorator=swagger_auto_schema(operation_id='Delete user', operation_summary='Delete user'))
class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
     get:
        get user
    put:
        all update user
    patch:
        update user
    delete:
        delete user
    """
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def get_permissions(self):
        return IsAdminUser(),


@method_decorator(name='patch',
                  decorator=swagger_auto_schema(operation_id='User unlocked', operation_summary='User unlocked'))
@method_decorator(name='put',
                  decorator=swagger_auto_schema(operation_id='User blocked', operation_summary='User blocked'))
class UserBlockedView(GenericAPIView):
    """
    patch:
        user unlocked
    put:
        user blocked
    """
    permission_classes = (IsManagerUser,)
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def patch(self, *args, **kwargs):
        user = self.get_object()
        UserModel.objects.to_active(user)
        user.save()
        data = UserModelSerializer(user).data
        return Response(data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        user = self.get_object()
        UserModel.objects.to_notactive(user)
        user.save()
        data = UserModelSerializer(user).data
        return Response(data, status.HTTP_200_OK)


@method_decorator(name='patch',
                  decorator=swagger_auto_schema(operation_id='Make user a manager',
                                                operation_summary='Make user a manager'))
@method_decorator(name='put',
                  decorator=swagger_auto_schema(operation_id='Make user not a manager',
                                                operation_summary='Make user not a manager'))
class UserToManagerView(GenericAPIView):
    """
    patch:
        make user a manager
    put:
        make user not a manager
    """
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def patch(self, *args, **kwargs):
        user = self.get_object()
        UserModel.objects.to_menager(user)
        user.save()
        data = UserModelSerializer(user).data
        return Response(data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        user = self.get_object()
        UserModel.objects.to_user(user)
        user.save()
        data = UserModelSerializer(user).data
        return Response(data, status.HTTP_200_OK)
