import datetime

from rest_framework.request import Request


class DateSelectionUtils:
    @classmethod
    def date_filter(cls, date_arrival_db: list, date_departure_db: list, request: Request):
        date_arrival = request.data['date_arrival']
        date_departure = request.data['date_departure']
        date_arrival = datetime.date(*[int(i) for i in date_arrival.split("-")])
        date_departure = datetime.date(*[int(i) for i in date_departure.split("-")])
        print(type(date_departure))
        list_arrival = []
        for date in date_arrival_db:
            list_arrival.append(date['date_arrival'])
        list_departure = []
        for i in date_departure_db:
            list_departure.append(i['date_departure'])

        # def a(x):
        #     return x >= date_arrival, list_arrival, print(x)
        #
        # def b(x):
        #     return x >= date_departure, list_departure, print(x)
        #
        # def start():
        #     if a and b:
        #         return True
        #     else:
        #         return False
        #
        # start()

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
