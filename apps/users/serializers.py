from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from .models import UserModel as User
from apps.apartments.serializers import ApartmentModelSerializer

UserModel: User = get_user_model()


class UserModelSerializer(ModelSerializer):
    apartment = ApartmentModelSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'name', 'surname', 'phone', 'password', 'is_active', 'is_staff', 'is_superuser',
            'last_login', 'created_at', 'updated_at', 'apartment'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
