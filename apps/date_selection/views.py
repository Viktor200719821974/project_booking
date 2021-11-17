import datetime
from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from .selializers import DateSelectionModelSerializer
from .models import DateSelectionModel
from apps.apartments.models import ApartmentModel
from exeptions.jwt_exeption import REQUESTException
from bookingApps.utils.date_selection_utils import DateSelectionUtils


class DateSelectionCreateView(CreateAPIView):
    queryset = DateSelectionModel.objects.all()
    serializer_class = DateSelectionModelSerializer

    def perform_create(self, serializer):
        pk = self.request.query_params.get('apartmentId')
        email = self.request.user
        price = ApartmentModel.objects.filter(pk=pk).values('price')[0].get('price')
        numbers_days = DateSelectionUtils.date_selection(self.request)
        cost = numbers_days * price
        exists = ApartmentModel.objects.filter(pk=pk).exists()
        if not exists:
            raise REQUESTException
        apartment = ApartmentModel.objects.get(pk=pk)
        serializer.save(apartment=apartment, user_email=email, number_days=numbers_days, cost=cost)


class DateSelectionRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = DateSelectionModel.objects.all()
    serializer_class = DateSelectionModelSerializer
