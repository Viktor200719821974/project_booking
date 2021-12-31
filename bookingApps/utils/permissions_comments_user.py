from apps.apartments.models import ApartmentModel
from apps.date_selection.models import DateSelectionModel
from apps.users.models import UserModel
from exeptions.jwt_exeption import AuthenticatedCommentUser


class PermissionsCommentsUser:
    @classmethod
    def permissions_comments_user(cls, pk, emailOwner):
        idOwner = UserModel.objects.filter(email=emailOwner).values('id')[0].get('id')
        emailUser = UserModel.objects.filter(id=pk).values('email')[0].get('email')
        existsDate = DateSelectionModel.objects.filter(user_email=emailUser).exists()
        if not existsDate:
            raise AuthenticatedCommentUser
        apartmentsIdUser = DateSelectionModel.objects.filter(user_email=emailUser).values('apartment_id')
        existsApartment = ApartmentModel.objects.filter(user_apartment_id=idOwner).exists()
        if not existsApartment:
            raise AuthenticatedCommentUser
        apartmentsIdOwner = ApartmentModel.objects.filter(user_apartment_id=idOwner).values('id')

        list_apartmentIdUser = []
        for i in apartmentsIdUser:
            list_apartmentIdUser.append(i['apartment_id'])

        list_apartmentIdOwner = []
        for i in apartmentsIdOwner:
            list_apartmentIdOwner.append(i['id'])

        def comparison():
            if list_apartmentIdUser == list_apartmentIdUser:
                return True
            else:
                return False

        return comparison()
        # all([x[i] == y[i] for i in range(len(x))])