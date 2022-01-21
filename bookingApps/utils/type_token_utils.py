import time
from datetime import datetime

from bookingApps.utils.email_utils import EmailUtils
from exeptions.jwt_exeption import NoRentException


class TypeToken:
    token_type = ' '

    @classmethod
    def type_token(cls, token_type):
        cls.token_type = token_type

    @classmethod
    def send_email_user(cls):
        type = cls.token_type
        return type

    @classmethod
    def send_email_sleep(cls, email, name: str, date_arrival: datetime, date_departure: datetime,
                         cost: float, number_days: datetime, number_peoples: int):

        start_time = time.time()
        CLOSE_AFTER = 300

        while True:

            type = TypeToken.send_email_user()
            if type == 'yes':
                EmailUtils.lease_confirmation_tenant(email, name=name, date_arrival=date_arrival,
                                                     date_departure=date_departure, cost=cost,
                                                     number_days=number_days,
                                                     number_peoples=number_peoples)
                break
            elif type == 'no' or time.time() > start_time + CLOSE_AFTER:
                EmailUtils.lease_confirmation_tenant_rent_no(email, name=name, date_arrival=date_arrival,
                                                             date_departure=date_departure)
                raise NoRentException



            else:
                continue

