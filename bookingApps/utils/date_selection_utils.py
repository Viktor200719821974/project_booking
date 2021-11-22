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
                return True, print('true_now')
            else:
                return False, print('false_now')

        def arrival1():
            for i in list_arrival:
                print(i)
                for j in list_departure:
                    print(j)
                    if i >= date_arrival < j and i > date_departure <= j:
                        return False, print('False_arrival1')
                    else:
                        continue
            return True, print('true_arrival1')

        # def arrival2():
        #     for i in list_arrival:
        #         print(i)
        #         for j in list_departure:
        #             print(j)
        #             if i < date_arrival >= j and i < date_departure > j:
        #                 return True, print('true_arrival2')
        #             else:
        #                 continue
        #     return False, print('false_arrival2')

        def arrival():
            if now() and arrival1():
                return True, print('true_arrival')
            else:
                return False, print('false_arrival')

        return arrival()

        # def departure1():
        #     for i in list_arrival:
        #         print(i)
        #         for j in list_departure:
        #             print(j)
        #             if i > date_departure > j:
        #                 return False, print('false_departure1')
        #             else:
        #                 continue
        #     return True, print('true_departure1')
        #
        # def departure2():
        #     for i in list_arrival:
        #         print(i)
        #         for j in list_departure:
        #             print(j)
        #             if i > date_departure < j:
        #                 return False, print('false_departure2')
        #             else:
        #                 continue
        #     return True, print('true_departure2')
        #
        # def departure():
        #     if departure1() == departure2():
        #         return True, print('true_departure')
        #     else:
        #         return False, print('false_departure')
        #
        # def start():
        #     if now() == arrival() == departure():
        #         return False
        #     else:
        #         return True
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
