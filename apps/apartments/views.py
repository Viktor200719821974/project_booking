# from django.utils.decorators import method_decorator
# from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import ApartmentModel
from .serializers import ApartmentModelSerializer, PhotoRoomsSerializer
from .filters import ApartmentFilter

# @method_decorator(name='get', decorator=swagger_auto_schema(operation_id='List of apartments', operation_summary='Get all'))
class ApartmentListCreateView(ListCreateAPIView):
    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentModelSerializer
    filterset_class = ApartmentFilter

    """
    get:
        Get all apartments
    post:
        Create apartment
    """

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
    """
     Get:
        get apartment
    Put:
        all update apartment
    Patch:
        update apartment
    Delete:
        delete apartment
    """
    def get_permissions(self):
        return IsAdminUser(),


class PhotoRoomsView(GenericAPIView):

    def patch(self, *args, **kwargs):
        photo_data = self.request.FILES.get('photo_rooms')
        serializer = PhotoRoomsSerializer(data={'url': photo_data})
        serializer.is_valid(raise_exception=True)
        pk = kwargs.get('pk')
        apartment = ApartmentModel.objects.get(pk=pk)
        serializer.save(apartment=apartment)
        apartment_serializer = ApartmentModelSerializer(apartment).data
        return Response(apartment_serializer, status.HTTP_200_OK)

