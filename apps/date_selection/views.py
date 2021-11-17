import datetime
from rest_framework.generics import GenericAPIView, CreateAPIView
from datetime import timedelta
from rest_framework.response import Response
from rest_framework import status

from .selializers import DateSelectionModelSerializer
from .models import DateSelectionModel
from apps.apartments.models import ApartmentModel
from exeptions.jwt_exeption import REQUESTException


class DateSelectionCreateView(CreateAPIView):
    queryset = DateSelectionModel.objects.all()
    serializer_class = DateSelectionModelSerializer

    def perform_create(self, serializer):
        pk = self.request.query_params.get('apartmentId')
        email = self.request.user
        price = ApartmentModel.objects.filter(pk=pk).values('price')[0].get('price')
        date_arrival = str(DateSelectionModel.objects.filter(pk=pk).values('date_arrival')[0].get('date_arrival'))
        date_departure = str(DateSelectionModel.objects.filter(pk=pk).values('date_departure')[0].get('date_departure'))
        date_arrival = datetime.date(*[int(i) for i in date_arrival.split("-")])
        date_departure = datetime.date(*[int(i) for i in date_departure.split("-")])
        numbers_days =str(date_departure - date_arrival)
        numbers_days = [int(i) for i in numbers_days.split() if i.isdigit()]
        numbers_days = numbers_days[0]
        cost = numbers_days * price
        exists = ApartmentModel.objects.filter(pk=pk).exists()
        if not exists:
            raise REQUESTException
        apartment = ApartmentModel.objects.get(pk=pk)
        serializer.save(apartment=apartment, user_email=email, number_days=numbers_days, cost= cost)

