from rest_framework.serializers import ModelSerializer

from .models import CommentsUserModel, PhotoModel


class PhotoCommentUserSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('url',)


class CommentsUserModelSerializer(ModelSerializer):
    photo_comments_user = PhotoCommentUserSerializer(many=True, read_only=True)

    class Meta:
        model = CommentsUserModel
        exclude = ('user', 'average_rating',)