from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from bookingApps.utils.jwt_utils import JwtUtils
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .serializers import EmailSerializer
from bookingApps.utils.email_utils import EmailUtils
from .serializers import PasswordSerializer
from enums.action_token import ActionTokenEnum
from apps.users.models import UserModel as User
from apps.users.serializers import UserModelSerializer

UserModel = get_user_model()


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_id='Activate user', operation_summary='Activate user'))
class ActivateView(GenericAPIView):
    """
    get:
        activate user
    """
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    @staticmethod
    def get(*args, **kwargs):
        token = kwargs.get('token')
        user = JwtUtils(ActionTokenEnum.ACTIVATE.token_type).validate_token(token)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


@method_decorator(name='post',
                  decorator=swagger_auto_schema(operation_id='Sending a request to change the password',
                                                operation_summary='Update password'))
@method_decorator(name='patch',
                  decorator=swagger_auto_schema(operation_id='Enter a token and a new password',
                                                operation_summary='New password'))
class RecoveryPasswordView(GenericAPIView):
    """
    post:
        sending a request to change the password
    patch:
        enter a token and a new password
    """
    serializer_class = UserModelSerializer
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        user = get_object_or_404(UserModel, email=email)
        token = JwtUtils(ActionTokenEnum.RECOVERY.token_type, ActionTokenEnum.RECOVERY.exp_time).create_token(user)
        EmailUtils.recovery_password_email(email, token, self.request)
        return Response(status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        data = self.request.data
        token = data.get('token')
        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        password = serializer.data.get('password')
        user: User = JwtUtils(ActionTokenEnum.RECOVERY.token_type).validate_token(token)
        user.set_password(password)
        user.save()
        return Response(status=status.HTTP_200_OK)
