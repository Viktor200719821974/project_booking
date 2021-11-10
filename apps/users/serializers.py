from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

from .models import UserModel as User
from apps.apartments.serializers import ApartmentModelSerializer
from apps.apartments.models import ApartmentModel
from apps.profile.serializers import ProfileSerializer
from apps.profile.models import ProfileModel

UserModel: User = get_user_model()


class UserModelSerializer(ModelSerializer):
    profile = ProfileSerializer()
    apartment = ApartmentModelSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at', 'profile', 'apartment'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        #     apartment = validated_data.pop('apartment')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        #     ApartmentModel.objects.create(**apartment, user=user)
        #     # token = JwtUtils(ActionTokenEnum.ACTIVATE.token_type, ActionTokenEnum.ACTIVATE.exp_time).create_token(user)
        #     # request = self.context.get('request')
        #     # EmailUtils.register_email(user.email, profile.get('name'), token, request)
        return user
