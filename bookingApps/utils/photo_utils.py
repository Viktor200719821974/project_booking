import os
from uuid import uuid1


class PhotoRoomsUtils:
    @staticmethod
    def upload_to(instance, file: str):
        ext = file.split('.')[-1]
        return os.path.join(instance.apartment.user_apartment.email, 'photo_rooms', f'{uuid1()}.{ext}')


class PhotoCommentApartmentUtils:
    @staticmethod
    def upload_to(instance, file: str):
        ext = file.split('.')[-1]
        return os.path.join(instance.photo.apartment.user_apartment.email, 'photo', f'{uuid1()}.{ext}')


class PhotoCommentUserUtils:
    @staticmethod
    def upload_to(instance, file: str):
        ext = file.split('.')[-1]
        return os.path.join(instance.photo.user.email, 'photo', f'{uuid1()}.{ext}')
