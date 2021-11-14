from rest_framework.serializers import ModelSerializer

from .models import CommentsApartmentModel, PhotoModel


class PhotoCommentApartmentSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('url',)


class CommentsApartmentModelSerializer(ModelSerializer):
    photo_comments_apartment = PhotoCommentApartmentSerializer(many=True, read_only=True)

    class Meta:
        model = CommentsApartmentModel
        exclude = ('apartment',)


