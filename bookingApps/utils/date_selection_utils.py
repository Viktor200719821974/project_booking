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

        def now():
            if date_arrival >= date_now and date_departure > date_now:
                return True
            else:
                return False

        def arrival():
            for i in list_arrival:
                print(i)
                if date_arrival < i and date_departure <= i:
                    return True
                else:
                    continue
            return False

        def department():
            for j in list_departure:
                print(j)
                if date_arrival >= j and date_departure > j:
                    return True
                else:
                    continue
            return False

        def date():
            if arrival() != department():
                return True
            else:
                return False

        def start():
            if now() == date():
                return True
            else:
                return False

        return start()

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
