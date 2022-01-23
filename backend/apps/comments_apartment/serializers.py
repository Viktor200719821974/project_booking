from rest_framework.serializers import ModelSerializer
from .models import CommentsApartmentModel, PhotoModelCommentsApartment


class PhotoCommentApartmentSerializer(ModelSerializer):
    class Meta:
        model = PhotoModelCommentsApartment
        fields = ('url', 'id',)
        extra_kwargs = {
            'id': {'read_only': True},
        }


class CommentsApartmentModelSerializer(ModelSerializer):
    photo_comments_apartment = PhotoCommentApartmentSerializer(many=True, read_only=True)

    class Meta:
        model = CommentsApartmentModel
        fields = ('apartment', 'comments', 'rating', 'photo_comments_apartment', 'name_user', 'id', 'user_id',
                  'user_email',)
        extra_kwargs = {
            'apartment': {'read_only': True},
            'id': {'read_only': True},
            'user_id': {'read_only': True},
            'user_email': {'read_only': True},
        }



