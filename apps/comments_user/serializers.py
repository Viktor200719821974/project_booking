from rest_framework.serializers import ModelSerializer

from .models import CommentsUserModel, PhotoModel


class PhotoCommentUserSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('url', 'id',)
        extra_kwargs = {
            'id': {'read_only': True},
        }


class CommentsUserModelSerializer(ModelSerializer):
    photo_comments_user = PhotoCommentUserSerializer(many=True, read_only=True)

    class Meta:
        model = CommentsUserModel
        fields = ('user', 'comments', 'rating', 'user_name', 'photo_comments_user', 'id',)
        extra_kwargs = {
            'user': {'read_only': True},
            'id': {'read_only': True},
        }