from rest_framework.serializers import ModelSerializer

from .models import CommentsApartmentModel, PhotoModel


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('url',)


class CommentsApartmentModelSerializer(ModelSerializer):
    photo_comments_apartment = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = CommentsApartmentModel
        exclude = ('apartment',)


