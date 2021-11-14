import django_filters as filters

from .models import ApartmentModel


class ApartmentFilter(filters.FilterSet):

    country_istartswith = filters.CharFilter('country', 'istartswith')
    country_iendswith = filters.CharFilter('country', 'iendswith')
    city_istartswith = filters.CharFilter('city', 'istartswith')
    city_iendswith = filters.CharFilter('city', 'iendswith')
    region_istartswith = filters.CharFilter('region', 'istartswith')
    region_iendswith = filters.CharFilter('city', 'iendswith')
    numbers_squares_gt = filters.NumberFilter('numbers_squares', 'gt')
    numbers_squares_lt = filters.NumberFilter('numbers_squares', 'lt')
    numbers_people_gt = filters.NumberFilter('numbers_people', 'gt')
    numbers_people_lt = filters.NumberFilter('numbers_people', 'lt')
    numbers_rooms_gt = filters.NumberFilter('numbers_rooms', 'gt')
    numbers_rooms_lt = filters.NumberFilter('numbers_rooms', 'lt')
    price_gt = filters.NumberFilter('price', 'gt')
    price_lt = filters.NumberFilter('price', 'lt')
    free_seats = filters.BooleanFilter('date_selection', 'free_seats__exact')

    class Meta:
        model = ApartmentModel
        fields = ('country', 'city', 'country_istartswith', 'country_iendswith', 'city_istartswith', 'city_iendswith',
                  'region_istartswith', 'region_iendswith', 'region', 'numbers_squares', 'numbers_squares_gt',
                  'numbers_squares_lt', 'numbers_people_gt', 'numbers_people_lt', 'numbers_people', 'numbers_rooms_gt',
                  'numbers_rooms_lt', 'numbers_rooms', 'price', 'price_gt', 'price_lt', 'free_seats',)
