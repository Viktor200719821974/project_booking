from django.db import models

from apps.apartments.models import ApartmentModel


# Create your models here.

class DateSelectionModel(models.Model):
    class Meta:
        db_table = 'date_selection'
        ordering = ('id',)

    date_arrival = models.DateField()
    date_departure = models.DateField()
    number_days = models.IntegerField()
    cost = models.FloatField()
    free_seats = models.BooleanField(default=False)
    user_email = models.EmailField()
    number_peoples = models.IntegerField()
    user_id = models.IntegerField(default=0)
    name_user = models.CharField(max_length=20, default='Anonymous')
    surname_user = models.CharField(max_length=20, default='Anonymous')
    apartment = models.ForeignKey(ApartmentModel, on_delete=models.CASCADE, related_name='date_selection')
