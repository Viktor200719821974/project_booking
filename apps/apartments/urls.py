from django.urls import path

from .views import  ApartmentListCreateView, ApartmentRetrieveUpdateDestroyView, PhotoRoomsView

urlpatterns = [
    path('', ApartmentListCreateView.as_view(), name='apartments_getAll_post'),
    path('/<int:pk>', ApartmentRetrieveUpdateDestroyView.as_view(), name='apartments_get_put_patch_delete'),
    path('/<int:pk>/photo_rooms', PhotoRoomsView.as_view(), name='apartments_add_photo_rooms'),
    # path('/<int:pk>/comments_apartment', ApartmentAddCommentView.as_view(), name='apartments_add_comments')
]