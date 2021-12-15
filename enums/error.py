from enum import Enum

from rest_framework import status


class ErrorEnum(Enum):
    JWT = ('Token expired or invalid', status.HTTP_403_FORBIDDEN)
    VLE1 = 'The email must be set'
    VLE2 = 'Superuser must have is_staff=True'
    VLE3 = 'Superuser must have is_superuser=True'
    REQUEST = 'Not Found'
    BADDATE = 'Sorry, but these days the apartment is busy'
    AUTHCOMAPARTMENT = ('Comments can leave only those who rented this housing', status.HTTP_403_FORBIDDEN)
    AUTHCOMUSER = ('Comments can leave only those who rented this housing', status.HTTP_403_FORBIDDEN)
    NORENT = ('has not been confirmed, you can choose another apartment', status.HTTP_418_IM_A_TEAPOT)
    ADDDELAPART = ('You do not have access rights because you are not the owner of this apartment',
                   status.HTTP_401_UNAUTHORIZED)

    def __init__(self, msg, code=status.HTTP_400_BAD_REQUEST):
        self.msg = msg
        self.code = code
