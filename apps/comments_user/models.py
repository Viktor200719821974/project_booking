from django.core import validators as V
from django.db import models

from apps.users.models import UserModel
from bookingApps.utils.photo_utils import PhotoCommentUserUtils


class CommentsUserModel(models.Model):
    class Meta:
        db_table = 'comments_user'
        ordering = ('id',)

    comments = models.CharField(max_length=200)
    rating = models.FloatField(max_length=3, validators=[V.MinValueValidator(1, 3), V.MaxValueValidator(5, 3)])
    average_rating = models.FloatField(default=0)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments_user')


class PhotoModel(models.Model):
    class Meta:
        db_table = 'photo_comments_user'

    url = models.ImageField(upload_to=PhotoCommentUserUtils.upload_to)
    photo = models.ForeignKey(CommentsUserModel, on_delete=models.CASCADE, related_name='photo_comments_user')
