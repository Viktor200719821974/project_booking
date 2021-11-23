from django.conf import settings
from django.db import models


class OutstandingApartmentToken(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False)
    apartment = models.ForeignKey(settings.APARTMENT_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    jti = models.CharField(unique=True, max_length=255)
    token = models.TextField()

    created_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/encode/django-rest-framework/issues/705
        abstract = 'rest_framework_simplejwt.token_blacklist' not in settings.INSTALLED_APPS
        ordering = ('apartment',)

    def __str__(self):
        return 'Token for {} ({})'.format(
            self.apartment,
            self.jti,
        )