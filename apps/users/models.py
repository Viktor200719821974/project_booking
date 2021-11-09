from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core import validators as V

from .managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'
        ordering = ('id',)

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=13, validators=[
        V.RegexValidator('^?=.*\+[0-9]{3}\s?[0-9]{2}\s?[0-9]{3}\s?[0-9]{4,5}$', 'пробелы разрешены, но не обязательны,'
                                                                                ' как указано ниже +380 99 678 3498')])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()
