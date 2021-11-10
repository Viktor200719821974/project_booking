from rest_framework.serializers import ModelSerializer

from .models import CommentsApartmentModel, PhotoModel
from apps.apartments.models import ApartmentModel


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('url',)


class CommentsApartmentModelSerializer(ModelSerializer):
    photo = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = CommentsApartmentModel
        exclude = ('apartment',)

    # def create(self, validated_data: dict):
    #     comments_apartment = validated_data.pop('comments_apartment')
