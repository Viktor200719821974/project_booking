import os
from typing import Iterable

from rest_framework.serializers import ModelSerializer

from bookingApps.utils.email_utils import EmailUtils
from .models import DateSelectionModel
from apps.users.models import UserModel
from apps.profile.models import ProfileModel
from apps.apartments.models import ApartmentModel


class DateSelectionModelSerializer(ModelSerializer):
    class Meta:
        model = DateSelectionModel
        exclude = ('apartment', 'number_days', 'user_email', 'cost',)

    def create(self, validated_data: dict):
        date_arrival = validated_data.get('date_arrival')
        date_departure = validated_data.get('date_departure')
        email = validated_data.get('user_email')
        cost = validated_data.get('cost')
        apartment  = validated_data
        print(apartment)
        # apartment = ApartmentModel.objects.filter(id=apartment_id).values('user_apartment_id')

        number_days = date_departure - date_arrival
        user_id = UserModel.objects.filter(email=email).values('id')[0].get('id')
        name = ProfileModel.objects.filter(user_id=user_id).values('name')[0].get('name')
        # EmailUtils.lease_confirmation_tenant(email, name=name, date_arrival=date_arrival, date_departure=date_departure,
        #                                      cost=cost, number_days=number_days)
        # EmailUtils.lease_confirmation_homeowner(email, name=name, date_arrival=date_arrival, date_departure=date_departure,
        #                                      cost=cost, number_days=number_days)
        return super().create(validated_data)
