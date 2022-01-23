from django.core import validators as V
from django.db import models

from apps.apartments.models import ApartmentModel
from bookingApps.utils.photo_utils import PhotoCommentApartmentUtils


class CommentsApartmentModel(models.Model):
    class Meta:
        db_table = 'comments_apartment'
        ordering = ('id',)

    comments = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(10)])
    name_user = models.CharField(max_length=30, default='Anonymous')
    user_id = models.IntegerField(default=0)
    user_email = models.EmailField(default='None')
    apartment = models.ForeignKey(ApartmentModel, on_delete=models.CASCADE, related_name='comments_apartment')


class PhotoModelCommentsApartment(models.Model):
    class Meta:
        db_table = 'photo_comments_apartment'

    url = models.ImageField(upload_to=PhotoCommentApartmentUtils.upload_to)
    photo = models.ForeignKey(CommentsApartmentModel, on_delete=models.CASCADE, related_name='photo_comments_apartment')
