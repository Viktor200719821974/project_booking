from rest_framework import status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import CommentsUserModel
from .serializers import CommentsUserModelSerializer, PhotoSerializer


class CommentsUserListCreateView(ListCreateAPIView):
    queryset = CommentsUserModel.objects.all()
    serializer_class = CommentsUserModelSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return AllowAny(),
        return IsAuthenticated(),


class CommentsUserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CommentsUserModel.objects.all()
    serializer_class = CommentsUserModelSerializer

    def get_permissions(self):
        return IsAdminUser(),


class PhotoView(GenericAPIView):

    def patch(self, *args, **kwargs):
        photo_data = self.request.FILES.get('photo')
        serializer = PhotoSerializer(data={'url': photo_data})
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=self.request.user.comments_user)
        user = CommentsUserModelSerializer(self.request.user).data
        return Response(user, status.HTTP_200_OK)
