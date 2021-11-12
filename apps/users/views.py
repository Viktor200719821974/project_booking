from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .serializers import UserModelSerializer
from .permissions import IsSuperUser, IsManagerUser
from apps.apartments.models import ApartmentModel
from apps.apartments.serializers import ApartmentModelSerializer

UserModel: User = get_user_model()


class UsersListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return AllowAny(),
        return IsAdminUser(),

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def get_serializer_context(self):
        return {'request':self.request}


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def get_permissions(self):
        return IsAdminUser(),


class UserBlockedView(GenericAPIView):
    permission_classes = (IsManagerUser,)
    queryset = UserModel.objects.all()

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


class UserToManagerView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

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


