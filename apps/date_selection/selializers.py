from rest_framework.serializers import ModelSerializer

from .models import DateSelectionModel


class DateSelectionModelSerializer(ModelSerializer):
    class Meta:
        model = DateSelectionModel
        exclude = ('apartment',)
 # ' number_days', 'user_email', 'cost',