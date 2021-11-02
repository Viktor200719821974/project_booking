from django.core import validators as V
from django.db import models

from bookingApps.utils.photo_rooms_utils import PhotoRoomsUtils


# Create your models here.
class ApartmentModel(models.Model):
    class Meta:
        db_table = 'apartments'
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартира'
        ordering = ('id',)

    country = models.CharField(max_length=30,
                               validators=[
                                   V.RegexValidator('^[A-Za-z]{,30}$', 'Country must be A-Z, a-z, max-length=30')])
    city = models.CharField(max_length=30,
                               validators=[
                                   V.RegexValidator('^[A-Za-z]{,30}$', 'City must be A-Z, a-z, max-length=30')])
    region = models.CharField(max_length=30,
                              validators=[
                                  V.RegexValidator('^[A-Za-z]{,30}$', 'Region must be A-Z, a-z, max-length=30')])
    numbers_squares = models.IntegerField(
                              validators=[V.MinValueValidator(30), 'Numbers of squares must be min value 30'])

    numbers_people = models.IntegerField(validators=[V.MinValueValidator(1), 'Numbers of people must be min value 1'])
    numbers_rooms = models.IntegerField(validators=[V.MinValueValidator(1), 'Numbers of rooms must be min value 1'])
    price = models.FloatField()
    # comments = models.CharField(
    #                           validators=[
    #                               V.RegexValidator('^[A-Za-z0-9]{,200}$', 'Comments must be A-Z, a-z, max-length=200')])


class PhotoRoomsModel(models.Model):
    class Meta:
        db_table = 'photo_rooms'

    url = models.ImageField(upload_to=PhotoRoomsUtils.upload_to)
    profile = models.ForeignKey(ApartmentModel, on_delete=models.CASCADE, related_name='photo_rooms')
