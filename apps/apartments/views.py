from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from bookingApps.utils.date_selection_utils import DateSelectionUtils
from .models import ApartmentModel, PhotoRoomsModel
from .serializers import ApartmentModelSerializer, PhotoRoomsSerializer
from .filters import ApartmentFilter
from exeptions.jwt_exeption import REQUESTException, BadDateException
from ..comments_apartment.models import CommentsApartmentModel
from ..comments_apartment.serializers import CommentsApartmentModelSerializer
from ..date_selection.models import DateSelectionModel
from ..date_selection.selializers import DateSelectionModelSerializer
from ..profile.models import ProfileModel
from ..users.models import UserModel
from ..users.permissions import CommentRentedApartment, AddDeleteApartment


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_id='List of apartments', operation_summary='Get all'))
@method_decorator(name='post',
                  decorator=swagger_auto_schema(operation_id='Create apartment',
                                                operation_summary='Create apartment'))
class ApartmentListCreateView(ListCreateAPIView):
    """
    get:
         Get all apartments
    post:
         Create apartment
    """
    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentModelSerializer
    filterset_class = ApartmentFilter

    def get_permissions(self):
        if self.request.method == 'POST':
            return IsAuthenticated(),
        return AllowAny(),

    def perform_create(self, serializer):
        user_id = self.request.user.id
        serializer.save(user_apartment_id=user_id)


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_id='Get of apartment', operation_summary='Get apartment'))
@method_decorator(name='put',
                  decorator=swagger_auto_schema(operation_id='All update of apartment', operation_summary='All update'))
@method_decorator(name='patch',
                  decorator=swagger_auto_schema(operation_id='Update apartment', operation_summary='Update apartment'))
@method_decorator(name='delete',
                  decorator=swagger_auto_schema(operation_id='Delete apartment', operation_summary='Delete apartment'))
class ApartmentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        get apartment
    put:
        all update apartment
    patch:
        update apartment
    delete:
        delete apartment
    """
    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return AllowAny(),
        return AddDeleteApartment(),


@method_decorator(name='patch',
                  decorator=swagger_auto_schema(operation_id='Add photo rooms', operation_summary='Add photo'))
class PhotoRoomsView(GenericAPIView):
    """
    patch:
        add photo rooms
    """
    serializer_class = PhotoRoomsSerializer
    queryset = PhotoRoomsModel.objects.all()

    def patch(self, *args, **kwargs):
        photo_data = self.request.FILES.get('photo_rooms')
        serializer = PhotoRoomsSerializer(data={'url': photo_data})
        serializer.is_valid(raise_exception=True)
        pk = kwargs.get('pk')
        apartment = ApartmentModel.objects.get(pk=pk)
        serializer.save(apartment=apartment)
        apartment_serializer = ApartmentModelSerializer(apartment).data
        return Response(apartment_serializer, status.HTTP_200_OK)


class PhotoRoomsDeletedView(RetrieveUpdateDestroyAPIView):
    """
    delete:
        delete photo rooms
    """
    serializer_class = PhotoRoomsSerializer
    queryset = PhotoRoomsModel.objects.all()

    def get_permissions(self):
        return IsAdminUser(),


@method_decorator(name='post',
                  decorator=swagger_auto_schema(operation_id='Selected date arrival and departure',
                                                operation_summary='Selected date'))
class DateSelectionCreateView(GenericAPIView):
    """
    post:
        selected date arrival and departure
    """
    queryset = DateSelectionModel.objects.all()
    serializer_class = DateSelectionModelSerializer

    def post(self, *args, **kwargs):
        pk = kwargs.get('pk')
        email = self.request.user
        data = self.request.data
        price = ApartmentModel.objects.filter(pk=pk).values('price')[0].get('price')
        userId = UserModel.objects.filter(email=email).values('id')[0].get('id')
        name = ProfileModel.objects.filter(user_id=userId).values('name')[0].get('name')
        surname = ProfileModel.objects.filter(user_id=userId).values('surname')[0].get('surname')
        if not name:
            return name == 'Anonymous'
        if not surname:
            return surname == 'Anonymous'
        numbers_days = DateSelectionUtils.date_selection(self.request)
        cost = numbers_days * price
        exists = ApartmentModel.objects.filter(pk=pk).exists()
        if not exists:
            raise REQUESTException
        else:
            free_seats = DateSelectionUtils.date_filter(pk, self.request)
            if not free_seats:
                raise BadDateException
        apartment = ApartmentModel.objects.get(pk=pk)
        serializer = DateSelectionModelSerializer(data=data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save(apartment=apartment, number_days=numbers_days, cost=cost, user_email=email,
                        free_seats=free_seats, user_id=userId, name_user=name, surname_user=surname)
        return Response(serializer.data, status.HTTP_201_CREATED)


@method_decorator(name='post',
                  decorator=swagger_auto_schema(operation_id='Create comments for apartment',
                                                operation_summary='Create comments for apartment'))
class CommentApartmentAddView(CreateAPIView):
    """
     post:
        Create comments apartment
    """
    queryset = CommentsApartmentModel.objects.all()
    serializer_class = CommentsApartmentModelSerializer
    permission_classes = (CommentRentedApartment,)

    def post(self, request, *args, **kwargs):
        userId = request.user.id
        user_email = request.user.email
        pk = kwargs.get('pk')
        data = self.request.data
        name = ProfileModel.objects.filter(user_id=userId).values('name')[0].get('name')
        exists = ApartmentModel.objects.filter(pk=pk).exists()
        if not exists:
            raise REQUESTException
        apartment = ApartmentModel.objects.get(pk=pk)
        serializer = CommentsApartmentModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(apartment=apartment, name_user=name, user_id=userId, user_email=user_email)
        return Response(serializer.data, status.HTTP_201_CREATED)
