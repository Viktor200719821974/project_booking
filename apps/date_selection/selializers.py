import time

from rest_framework.serializers import ModelSerializer

from bookingApps.utils.email_utils import EmailUtils
from bookingApps.utils.jwt_utils import JwtUtils
from bookingApps.utils.rating_utils import AverageRating
from bookingApps.utils.type_token_utils import TypeToken
from enums.action_token import ActionTokenEnum
from exeptions.jwt_exeption import NoRentException
from .models import DateSelectionModel
from apps.users.models import UserModel
from apps.profile.models import ProfileModel
from apps.apartments.models import ApartmentModel
from apps.comments_user.models import CommentsUserModel


class DateSelectionModelSerializer(ModelSerializer):
    class Meta:
        model = DateSelectionModel
        fields = ('id', 'apartment', 'date_arrival', 'date_departure', 'number_days', 'cost', 'user_email',
                  'number_peoples',)
        extra_kwargs = {
            'apartment': {'read_only': True},
            'id': {'read_only': True},
            'cost': {'read_only': True},
            'number_days': {'read_only': True},
            'user_email': {'read_only': True},
        }
        # exclude = ('apartment', 'number_days', 'user_email', 'cost',)

    def create(self, validated_data: dict):
        request = self.context.get('request')
        date_arrival = validated_data.get('date_arrival')
        date_departure = validated_data.get('date_departure')
        email = validated_data.get('user_email')
        cost = validated_data.get('cost')
        number_peoples = validated_data.get('number_peoples')
        pk = validated_data.get('apartment').id
        user_apartment_id = ApartmentModel.objects.filter(pk=pk).values('user_apartment')[0].get('user_apartment')
        user = validated_data.get('user_email')
        email_apartment = UserModel.objects.filter(pk=user_apartment_id).values('email')[0].get('email')
        token_yes = JwtUtils(ActionTokenEnum.YES.token_type, ActionTokenEnum.YES.exp_time).create_token(user)
        token_no = JwtUtils(ActionTokenEnum.NO.token_type, ActionTokenEnum.NO.exp_time).create_token(user)
        name_apartment = ProfileModel.objects.filter(user_id=user_apartment_id).values('name')[0].get('name')
        number_days = date_departure - date_arrival
        user_id = UserModel.objects.filter(email=email).values('id')[0].get('id')
        name = ProfileModel.objects.filter(user_id=user_id).values('name')[0].get('name')
        surname = ProfileModel.objects.filter(user_id=user_id).values('surname')[0].get('surname')
        age_user = ProfileModel.objects.filter(user_id=user_id).values('age')[0].get('age')
        phone_user = ProfileModel.objects.filter(user_id=user_id).values('phone')[0].get('phone')
        average_rating = AverageRating.average_rating_user(pk=user_id)
        EmailUtils.lease_confirmation_homeowner(email_apartment, name=name_apartment, date_arrival=date_arrival,
                                                date_departure=date_departure, cost=cost, number_days=number_days,
                                                number_peoples=number_peoples, name_user=name, surname_user=surname,
                                                age_user=age_user, phone_user=phone_user,
                                                average_rating=average_rating, token_yes=token_yes, token_no=token_no,
                                                request=request)

        TypeToken.send_email_sleep(email, name=name, date_arrival=date_arrival,date_departure=date_departure,
                                   cost=cost, number_days=number_days,number_peoples=number_peoples)
        type_token = TypeToken.send_email_user()
        if type_token == 'yes':
            EmailUtils.lease_confirmation_tenant(email, name=name, date_arrival=date_arrival,
                                                 date_departure=date_departure, cost=cost, number_days=number_days,
                                                 number_peoples=number_peoples)
        else:
            EmailUtils.lease_confirmation_tenant_rent_no(email, name=name, date_arrival=date_arrival,
                                                         date_departure=date_departure)
            raise NoRentException

        return super().create(validated_data)
