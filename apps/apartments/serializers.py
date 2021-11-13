from rest_framework.serializers import ModelSerializer

from .models import ApartmentModel, PhotoRoomsModel
from apps.comments_apartment.serializers import CommentsApartmentModelSerializer
from apps.date_selection.selializers import DateSelectionModelSerializer


class PhotoRoomsSerializer(ModelSerializer):
    class Meta:
        model = PhotoRoomsModel
        fields = ('url',)


class ApartmentModelSerializer(ModelSerializer):
    photo_rooms = PhotoRoomsSerializer(many=True, read_only=True)
    comments_apartment = CommentsApartmentModelSerializer(many=True, read_only=True)
    date_selection = DateSelectionModelSerializer(many=True, read_only=True)

    class Meta:
        model = ApartmentModel
        exclude = ('user_apartment',)
