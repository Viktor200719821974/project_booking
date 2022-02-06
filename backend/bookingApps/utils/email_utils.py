import datetime
import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from rest_framework.request import Request
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import Token

from enums.email_template import TemplateEnum


class EmailUtils:
    @staticmethod
    def _send_mail(to: str, template_name: str, context: dict, subject='') -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def register_email(cls, address: str, name: str, token: Token, request: Request) -> None:
        # uri = request.build_absolute_uri('http://localhost:3000/register/activate/', token)
        cls._send_mail(address, TemplateEnum.REGISTER.value,
                       {'name': name, "url": 'http://localhost:3000/register/activate/' + str(token)}, 'Register')

    @classmethod
    def recovery_password_email(cls, address: str, token: Token, request: Request) -> None:
        uri = request.build_absolute_uri(reverse('auth_recovery_password'))
        cls._send_mail(address, TemplateEnum.RECOVERY_PASSWORD.value, {'token': token, "url": uri}, 'Recovery password')

    @classmethod
    def lease_confirmation_tenant(cls, address: str, name: str, date_arrival: datetime, date_departure: datetime,
                                  cost: float, number_days: datetime, number_peoples: int) -> None:
        cls._send_mail(address, TemplateEnum.TENANT.value, {'name': name, 'date_arrival': date_arrival,
                                                            'date_departure': date_departure,
                                                            'number_days': number_days, 'cost': cost,
                                                            'number_peoples': number_peoples}, 'Tenant')

    @classmethod
    def lease_confirmation_tenant_rent_no(cls, address: str, name: str, date_arrival: datetime,
                                          date_departure: datetime, ) -> None:
        cls._send_mail(address, TemplateEnum.TENANT_NO_RENT.value, {'name': name, 'date_arrival': date_arrival,
                                                                    'date_departure': date_departure}, 'Tenant No Rent')

    @classmethod
    def lease_confirmation_homeowner(cls, address: str, name: str, date_arrival: datetime, date_departure: datetime,
                                     cost: float, number_days: datetime, number_peoples: int, name_user: str,
                                     surname_user: str, age_user: int, phone_user: str, average_rating: float,
                                     token_no: Token, token_yes: Token, pk: int, user_id: int,
                                     request: Request) -> None:
        # uri_yes = request.build_absolute_uri(reverse('date_selection_yes', args=(token_yes,)))
        # uri_no = request.build_absolute_uri(reverse('date_selection_no', args=(token_no,)))
        cls._send_mail(address, TemplateEnum.HOMEOWNER.value, {'name': name, 'date_arrival': date_arrival,
                                                               'date_departure': date_departure,
                                                               'number_days': number_days, 'cost': cost,
                                                               'number_peoples': number_peoples, 'name_user': name_user,
                                                               'surname_user': surname_user, 'age_user': age_user,
                                                               'phone_user': phone_user, 'average_rating':
                                                                   average_rating,
                                                               'url_yes': 'http://localhost:3000/activate/yes/' + str(
                                                                   pk) + '/' + str(user_id) + '/' +
                                                                          str(token_yes),
                                                               'url_no': 'http://localhost:3000/activate/no/'
                                                                         + str(pk) + '/' + str(user_id) + '/'
                                                                         + str(token_no)}, 'Homeowner')
