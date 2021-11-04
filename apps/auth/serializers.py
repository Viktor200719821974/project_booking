from django.contrib.auth import get_user_model

from rest_framework import serializers

UserModel = get_user_model()


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ('email',)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('password',)