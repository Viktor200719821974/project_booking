from django.core import validators as V
from django.db import models

from apps.apartments.models import ApartmentModel
from bookingApps.utils.photo_rooms_utils import PhotoUtils


class CommentsApartmentModel(models.Model):
    class Meta:
        db_table = 'comments_apartment'
        ordering = ('id',)

    comments = models.CharField(max_length=200,
        validators=[
            V.RegexValidator('^[A-Za-z0-9]{,200}$', 'Comments must be A-Z, a-z, max-length=200')])
    rating = models.FloatField(max_length=3, validators=[V.MinValueValidator(1, 3), V.MaxValueValidator(5, 3)])
    apartments = models.OneToOneField(ApartmentModel, on_delete=models.CASCADE, related_name='comments_apartment')


class PhotoModel(models.Model):
    class Meta:
        db_table = 'photo_comments_apartment'

    url = models.ImageField(upload_to=PhotoUtils.upload_to)
    photo = models.ForeignKey(CommentsApartmentModel, on_delete=models.CASCADE, related_name='photo_comments_apartment')
