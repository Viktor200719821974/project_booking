from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import ApartmentModel
from .serializers import ApartmentModelSerializer, PhotoRoomsSerializer


class ApartmentListCreateView(ListCreateAPIView):
    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentModelSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return IsAuthenticated(),
        return AllowAny(),


class ApartmentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentModelSerializer

    def get_permissions(self):
        return IsAdminUser(),


class PhotoRoomsView(GenericAPIView):

    def patch(self, *args, **kwargs):
        photo_data = self.request.FILES.get('photo_rooms')
        serializer = PhotoRoomsSerializer(data={'url': photo_data})
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=self.request.apartment)
        apartment = ApartmentModelSerializer(self.request.apartment).data
        return Response(apartment, status.HTTP_200_OK)
