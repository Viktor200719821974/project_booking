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

    def perform_create(self, serializer):
        user_id = self.request.user.id
        serializer.save(user_apartment_id=user_id)


class ApartmentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentModelSerializer

    def get_permissions(self):
        return IsAdminUser(),


class PhotoRoomsView(GenericAPIView):

    def patch(self, *args, **kwargs):
        photo_data = self.request.FILES.get('photo_rooms')
        serializer = PhotoRoomsSerializer(data={'url': photo_data})
        print(self.request)
        serializer.is_valid(raise_exception=True)
        print(self.request.apartments.user)
        serializer.save(apartment=self.request.apartments.user)
        print('hello')
        apartment = ApartmentModelSerializer(self.request.apartments).data
        return Response(apartment, status.HTTP_200_OK)
