from datetime import timedelta
from typing import Optional

from rest_framework_simplejwt.tokens import Token, BlacklistMixin
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from django.contrib.auth import get_user_model

from exeptions.jwt_exeption import JwtException

UserModel = get_user_model()


class _ActionToken(BlacklistMixin, Token):
    lifetime = timedelta(hours=24)


class JwtUtils:
    def __init__(self, token_type: str, life_time: Optional[timedelta] = None, token_class=_ActionToken):
        self._TokenClass = token_class
        if life_time:
            self._TokenClass.lifetime = life_time
        self._TokenClass.token_type = token_type

    def create_token(self, user):
        return self._TokenClass.for_user(user)

    def validate_token(self, token):
        try:
            action_token = self._TokenClass(token)
            if not OutstandingToken.objects.filter(token=token).exists():
                raise JwtException
            action_token.check_blacklist()
            action_token.blacklist()
            user_id = action_token.payload.get('user_id')
            return UserModel.objects.get(pk=user_id)
        except Exception:
            raise JwtException

    def validate_apartment_token(self, token):
        try:
            apartment_token = self._TokenClass(token)
            token_type = self._TokenClass.token_type
            if not OutstandingToken.objects.filter(token=token).exists():
                raise JwtException
            apartment_token.check_blacklist()
            apartment_token.blacklist()
            return token_type
        except Exception:
            raise JwtException

