from rest_framework.serializers import ModelSerializer

from .models import ApartmentModel, PhotoRoomsModel


class PhotoRoomsSerializer(ModelSerializer):
    class Meta:
        model = PhotoRoomsModel
        fields = ('url',)


class ApartmentModelSerializer(ModelSerializer):
    photo_rooms = PhotoRoomsSerializer(many=True, read_only=True)

    class Meta:
        model = ApartmentModel
        fields = '__all__'
