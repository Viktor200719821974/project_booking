from apps.comments_apartment.models import CommentsApartmentModel
from apps.comments_user.models import CommentsUserModel


class AverageRating:
    @classmethod
    def average_rating_apartment(cls, pk):
        rating_apartment_db = CommentsApartmentModel.objects.filter(apartment_id=pk).values('rating')
        list_rating_apartment = []
        for i in rating_apartment_db:
            list_rating_apartment.append(i['rating'])
        print(list_rating_apartment)
        average = sum(list_rating_apartment) / len(list_rating_apartment)
        return round(average, 0)

    @classmethod
    def average_rating_user(cls, pk):
        rating_user_db = CommentsUserModel.objects.filter(user_id=pk).values('rating')
        list_rating_user = []
        for i in rating_user_db:
            list_rating_user.append(i['rating'])
        average = sum(list_rating_user) / len(list_rating_user)
        return round(average, 2)
