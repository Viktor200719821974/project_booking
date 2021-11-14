from django.contrib.auth.base_user import BaseUserManager

from exeptions.jwt_exeption import Vle1Exception, Vle2Exception, Vle3Exception


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_kwargs):
        if not email:
            # raise ValueError("The email must be set")
            raise Vle1Exception
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_kwargs):
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_active', True)

        if extra_kwargs.get('is_staff') is not True:
            # raise ValueError('Superuser must have is_staff=True')
            raise Vle2Exception
        if extra_kwargs.get('is_superuser') is not True:
            # raise ValueError('Superuser must have is_superuser=True')
            raise Vle3Exception
        user = self.create_user(email, password, **extra_kwargs)
        return user

    @staticmethod
    def to_menager(user):
        user.is_staff = True
        user.save()

    @staticmethod
    def to_user(user):
        user.is_staff = False
        user.save()

    @staticmethod
    def to_active(user):
        user.is_active = True
        user.save()

    @staticmethod
    def to_notactive(user):
        user.is_active = False
        user.save()