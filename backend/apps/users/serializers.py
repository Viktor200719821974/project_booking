from django.contrib.auth import get_user_model
from rest_framework.response import Response

from rest_framework.serializers import ModelSerializer

from bookingApps.utils.email_utils import EmailUtils
from bookingApps.utils.jwt_utils import JwtUtils
from enums.action_token import ActionTokenEnum
from .models import UserModel as User
from apps.apartments.serializers import ApartmentModelSerializer
from apps.profile.serializers import ProfileSerializer
from apps.profile.models import ProfileModel
from apps.comments_user.serializers import CommentsUserModelSerializer

UserModel: User = get_user_model()


class UserModelSerializer(ModelSerializer):
    profile = ProfileSerializer()
    apartment = ApartmentModelSerializer(many=True, read_only=True)
    comments_user = CommentsUserModelSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at', 'profile', 'apartment', 'comments_user',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        # token = JwtUtils(ActionTokenEnum.ACTIVATE.token_type, ActionTokenEnum.ACTIVATE.exp_time).create_token(user)
        # request = self.context.get('request')
        # EmailUtils.register_email(user.email, profile.get('name'), token, request)
        return user
