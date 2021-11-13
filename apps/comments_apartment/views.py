from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import CommentsApartmentModel
from .serializers import CommentsApartmentModelSerializer, PhotoSerializer
from apps.apartments.models import ApartmentModel
from exeptions.jwt_exeption import REQUESTException


class CommentsApartmentListCreateView(ListCreateAPIView):
    queryset = CommentsApartmentModel.objects.all()
    serializer_class = CommentsApartmentModelSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return IsAuthenticated(),
        return AllowAny(),

    def perform_create(self, serializer):
        pk = self.request.query_params.get('apartmentId')
        exists = ApartmentModel.objects.filter(pk=pk).exists()
        if not exists:
            raise REQUESTException
        apartment = ApartmentModel.objects.get(pk=pk)
        serializer.save(apartment=apartment)


class CommentsApartmentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CommentsApartmentModel.objects.all()
    serializer_class = CommentsApartmentModelSerializer

    def get_permissions(self):
        return IsAdminUser(),


class PhotoCommentApartmentView(GenericAPIView):

    def patch(self, *args, **kwargs):
        photo_data = self.request.FILES.get('photo_comments_apartment')
        serializer = PhotoSerializer(data={'url': photo_data})
        serializer.is_valid(raise_exception=True)
        pk = kwargs.get('pk')
        comment_photo = CommentsApartmentModel.objects.get(pk=pk)
        serializer.save(photo=comment_photo)
        comment_photo_serializer = CommentsApartmentModelSerializer(comment_photo).data
        return Response(comment_photo_serializer, status.HTTP_200_OK)

