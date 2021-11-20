import datetime

from rest_framework.request import Request


class DateSelectionUtils:
    @classmethod
    def date_filter(cls, date_arrival_db: list, date_departure_db: list, request: Request):
        date_arrival = request.data['date_arrival']
        date_departure = request.data['date_departure']
        date_arrival = datetime.date(*[int(i) for i in date_arrival.split("-")])
        date_departure = datetime.date(*[int(i) for i in date_departure.split("-")])
        list_arrival = []
        for i in date_arrival_db:
            list_arrival.append(i['date_arrival'])
        list_departure = []
        for i in date_departure_db:
            list_departure.append(i['date_departure'])
        date_now = datetime.date.today()

        def now():
            if date_arrival >= date_now and date_departure > date_now:
                return True, print('true_now')
            else:
                return False, print('false_now')

        def arrival():
            # return date_departure <= x > date_arrival, list_arrival
            for i in range(len(list_arrival)):
                print(list_arrival[i])
                if date_arrival > list_arrival[i] <= date_departure:
                    return True, print('true_arrival')
                else:
                    return False, print('false_arrival')

        def departure():
            # return date_arrival >= x < date_departure, list_departure
            for i in list_departure:
                print(i)
                if date_arrival >= i < date_departure:
                    return True, print('true_departure')
                else:
                    return False, print('false_departure')

        def start():
            if now() and arrival() and departure():
                return False
            else:
                return True

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
