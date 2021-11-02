from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response

from .models import ApartmentModel
from .serializers import ApartmentModelSerializer, PhotoRoomsSerializer


class AppartmentListCreateView(ListCreateAPIView):
    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentModelSerializer


class ApartmentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentModelSerializer


class PhotoRoomsView(GenericAPIView):

    def patch(self, *args, **kwargs):
        photo_data = self.request.FILES.get('photo_rooms')
        serializer = PhotoRoomsSerializer(data={'url': photo_data})
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=self.request.user.apartment)
        user = ApartmentModelSerializer(self.request.user).data
        return Response(user, status.HTTP_200_OK)
