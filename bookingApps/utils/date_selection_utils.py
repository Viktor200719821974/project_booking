import datetime

from rest_framework.request import Request

from apps.date_selection.models import DateSelectionModel


class DateSelectionUtils:
    @classmethod
    def date_filter(cls, pk, request: Request):
        date_arrival = request.data['date_arrival']
        date_departure = request.data['date_departure']
        date_arrival = datetime.date(*[int(i) for i in date_arrival.split("-")])
        date_departure = datetime.date(*[int(i) for i in date_departure.split("-")])
        date_arrival_db = DateSelectionModel.objects.filter(apartment_id=pk).values('date_arrival')
        date_departure_db = DateSelectionModel.objects.filter(apartment_id=pk).values('date_departure')
        list_arrival = []
        for i in date_arrival_db:
            list_arrival.append(i['date_arrival'])
        list_departure = []
        for i in date_departure_db:
            list_departure.append(i['date_departure'])
        date_now = datetime.date.today()
        arrival = DateSelectionModel.objects.filter(date_arrival__gt=date_arrival).filter(date_departure__gte=date_departure).exists()
        print('arrival:',arrival)
        if not arrival:
            arrival1 = DateSelectionModel.objects.filter(date_arrival__lt=date_arrival).filter(date_departure__lt=date_arrival).exists()
            # departure = DateSelectionModel.objects.filter(date_departure__lt=date_arrival).filter(date_departure__lt=date_departure).exists()
            print('departure:', arrival1)
            if not arrival1:
                return False
        return True
        # def now():
        #     if date_arrival >= date_now and date_departure > date_now:
        #         return True, print('true_now')
        #     else:
        #         return False, print('false_now')
        #
        # def arrival():
        #     for i in list_arrival:
        #         print(i)
        #         if date_arrival < i and date_departure <= i:
        #             return True, print('true_arrival1')
        #         else:
        #             continue
        #     return False, print('false_arrival1')
        #
        # def department():
        #     for j in list_departure:
        #         print(j)
        #         if date_arrival >= j and date_departure > j:
        #             return True, print('true_departure')
        #         else:
        #             continue
        #     return False, print('false_departure')
        #
        # def date():
        #     if arrival() != department():
        #         return True, print('true_date')
        #     else:
        #         return False, print('false_date')
        #
        # def start():
        #     if now() == date():
        #         return True
        #     else:
        #         return False
        #
        # return start()

    @classmethod
    def date_selection(cls, request: Request):
        date_arrival = request.data['date_arrival']
        date_departure = request.data['date_departure']
        date_arrival = datetime.date(*[int(i) for i in date_arrival.split("-")])
        date_departure = datetime.date(*[int(i) for i in date_departure.split("-")])
        numbers_days = str(date_departure - date_arrival)
        numbers_days = [int(i) for i in numbers_days.split() if i.isdigit()]
        numbers_days = numbers_days[0]
        return numbers_days
