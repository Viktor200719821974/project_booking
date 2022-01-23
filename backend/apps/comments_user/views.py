from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import CommentsUserModel, PhotoModel
from .serializers import CommentsUserModelSerializer, PhotoCommentUserSerializer


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_id='List comments for user', operation_summary='Get all'))
class CommentsUserListView(ListAPIView):
    """
     get:
         Get all comments user
    """
    queryset = CommentsUserModel.objects.all()
    serializer_class = CommentsUserModelSerializer

    def get_permissions(self):
        return IsAdminUser(),


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_id='Get comment for user',
                                                operation_summary='Get comment for user'))
@method_decorator(name='put',
                  decorator=swagger_auto_schema(operation_id='All update comment for user',
                                                operation_summary='All update'))
@method_decorator(name='patch',
                  decorator=swagger_auto_schema(operation_id='Update comment for user',
                                                operation_summary='Update comment for user'))
@method_decorator(name='delete',
                  decorator=swagger_auto_schema(operation_id='Delete comments for user',
                                                operation_summary='Delete comments for user'))
class CommentsUserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        get comments user
    put:
        all update comments user
    patch:
        update comments user
    delete:
        delete comments user
    """
    queryset = CommentsUserModel.objects.all()
    serializer_class = CommentsUserModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return IsAuthenticated(),
        return IsAdminUser(),


@method_decorator(name='patch',
                  decorator=swagger_auto_schema(operation_id='Add photo for comments user',
                                                operation_summary='Add photo'))
class PhotoCommentUserView(GenericAPIView):
    """
    patch:
        add photo for comments user
    """
    serializer_class = PhotoCommentUserSerializer
    queryset = PhotoModel.objects.all()

    def patch(self, *args, **kwargs):
        photo_data = self.request.FILES.get('photo_comments_user')
        serializer = PhotoCommentUserSerializer(data={'url': photo_data})
        serializer.is_valid(raise_exception=True)
        pk = kwargs.get('pk')
        comment_photo = CommentsUserModel.objects.get(pk=pk)
        serializer.save(photo=comment_photo)
        comment_photo_serializer = CommentsUserModelSerializer(comment_photo).data
        return Response(comment_photo_serializer, status.HTTP_200_OK)


class PhotoCommentUserDeletedView(RetrieveUpdateDestroyAPIView):
    """
    delete:
        delete photo comment user
    """
    serializer_class = PhotoCommentUserSerializer
    queryset = PhotoModel.objects.all()

    def get_permissions(self):
        return IsAdminUser(),
