from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import CommentsUserModel
from .serializers import CommentsUserModelSerializer, PhotoSerializer
from apps.users.models import UserModel
from exeptions.jwt_exeption import REQUESTException


class CommentsUserListCreateView(ListCreateAPIView):
    queryset = CommentsUserModel.objects.all()
    serializer_class = CommentsUserModelSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return IsAuthenticated(),
        return AllowAny(),

    def perform_create(self, serializer):
        pk = self.request.query_params.get('userId')
        exists = UserModel.objects.filter(pk=pk).exists()
        if not exists:
            raise REQUESTException
        user = UserModel.objects.get(pk=pk)
        serializer.save(user=user)


class CommentsUserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CommentsUserModel.objects.all()
    serializer_class = CommentsUserModelSerializer

    def get_permissions(self):
        return IsAdminUser(),


class PhotoCommentUserView(GenericAPIView):

    def patch(self, *args, **kwargs):
        photo_data = self.request.FILES.get('photo_comments_user')
        serializer = PhotoSerializer(data={'url': photo_data})
        serializer.is_valid(raise_exception=True)
        pk = kwargs.get('pk')
        comment_photo = CommentsUserModel.objects.get(pk=pk)
        serializer.save(photo=comment_photo)
        comment_photo_serializer = CommentsUserModelSerializer(comment_photo).data
        return Response(comment_photo_serializer, status.HTTP_200_OK)
