from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser

from exeptions.jwt_exeption import REQUESTException
from .models import CommentsApartmentModel
from .serializers import CommentsApartmentModelSerializer, PhotoCommentApartmentSerializer
from .models import PhotoModel


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_id='List comments for user', operation_summary='Get all'))
class CommentsApartmentListView(ListAPIView):
    """
     get:
         Get all comments user
    """
    queryset = CommentsApartmentModel.objects.all()
    serializer_class = CommentsApartmentModelSerializer

    def get_permissions(self):
        return AllowAny(),


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_id='Get comment for apartment',
                                                operation_summary='Get comment for apartment'))
@method_decorator(name='put',
                  decorator=swagger_auto_schema(operation_id='All update comment for apartment',
                                                operation_summary='All update'))
@method_decorator(name='patch',
                  decorator=swagger_auto_schema(operation_id='Update comment for apartment',
                                                operation_summary='Update comment for apartment'))
@method_decorator(name='delete',
                  decorator=swagger_auto_schema(operation_id='Delete comments for apartment',
                                                operation_summary='Delete comments for apartment'))
class CommentsApartmentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        get comments apartment
    put:
        all update comments apartment
    patch:
        update comments apartment
    delete:
        delete comments apartment
    """
    queryset = CommentsApartmentModel.objects.all()
    serializer_class = CommentsApartmentModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return AllowAny(),
        return IsAdminUser(),


@method_decorator(name='patch',
                  decorator=swagger_auto_schema(operation_id='Add photo for comments apartment',
                                                operation_summary='Add photo'))
class PhotoCommentApartmentView(GenericAPIView):
    """
    patch:
        add photo for comments apartment
    """
    serializer_class = PhotoCommentApartmentSerializer
    queryset = PhotoModel.objects.all()

    def patch(self, *args, **kwargs):
        photo_data = self.request.FILES.get('photo_comments_apartment')
        serializer = PhotoCommentApartmentSerializer(data={'url': photo_data})
        serializer.is_valid(raise_exception=True)
        pk = kwargs.get('pk')
        exists = PhotoModel.objects.filter(pk=pk).exists()
        if not exists:
            raise REQUESTException
        comment_photo = CommentsApartmentModel.objects.get(pk=pk)
        serializer.save(photo=comment_photo)
        comment_photo_serializer = CommentsApartmentModelSerializer(comment_photo).data
        return Response(comment_photo_serializer, status.HTTP_200_OK)
