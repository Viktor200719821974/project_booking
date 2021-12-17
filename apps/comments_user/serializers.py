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
        fields = ('user', 'comments', 'rating', 'user_name', 'photo_comments_user', 'average_rating',)
        extra_kwargs = {
            'user': {'read_only': True},
            'average_rating': {'read_only': True},
        }