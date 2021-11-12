from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import CommentsApartmentModel
from .serializers import CommentsApartmentModelSerializer, PhotoSerializer


class CommentsApartmentListCreateView(ListCreateAPIView):
    queryset = CommentsApartmentModel.objects.all()
    serializer_class = CommentsApartmentModelSerializer

    def get_permissions(self):
        return AllowAny(),

    def perform_create(self, serializer):
        apartment_id = self.request.query_params.get('apartmentId')
        print(apartment_id)
        serializer.save(apartments_id=apartment_id)


class CommentsApartmentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CommentsApartmentModel.objects.all()
    serializer_class = CommentsApartmentModelSerializer

    def get_permissions(self):
        return IsAdminUser(),


class PhotoView(GenericAPIView):

    def patch(self, *args, **kwargs):
        photo_data = self.request.FILES.get('photo')
        serializer = PhotoSerializer(data={'url': photo_data})
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=self.request.apartment.comments_apartment)
        apartment = CommentsApartmentModelSerializer(self.request.apartment).data
        return Response(apartment, status.HTTP_200_OK)
