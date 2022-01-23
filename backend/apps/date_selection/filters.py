import django_filters as filters

from .models import DateSelectionModel


class DateFilter(filters.FilterSet):
    date_arrival_gt = filters.DateFilter('date_arrival', 'gt')
    date_arrival_gte = filters.DateFilter('date_arrival', 'gte')
    date_arrival_lt = filters.DateFilter('date_arrival', 'lt')
    date_arrival_lte = filters.DateFilter('date_arrival', 'lte')
    date_departure_gt = filters.DateFilter('date_departure', 'gt')
    date_departure_gte = filters.DateFilter('date_departure', 'gte')
    date_departure_lt = filters.DateFilter('date_departure', 'lt')
    date_departure_lte = filters.DateFilter('date_departure', 'lte')

    class Meta:
        model = DateSelectionModel
        fields = ('date_departure_lt', 'date_departure_lte', 'date_departure_gt', 'date_departure_gte',
                  'date_departure', 'date_arrival_gte', 'date_arrival_gt', 'date_arrival_lte', 'date_arrival_lt',
                  'apartment_id', 'date_arrival',)
