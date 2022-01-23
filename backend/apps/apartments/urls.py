from django.urls import path

from .views import ApartmentListCreateView, ApartmentRetrieveUpdateDestroyView, PhotoRoomsView, \
    DateSelectionCreateView, CommentApartmentAddView, PhotoRoomsDeletedView

urlpatterns = [
    path('', ApartmentListCreateView.as_view(), name='apartments_getAll_post'),
    path('/<int:pk>', ApartmentRetrieveUpdateDestroyView.as_view(), name='apartments_get_put_patch_delete'),
    path('/<int:pk>/photo_rooms', PhotoRoomsView.as_view(), name='apartments_add_photo_rooms'),
    path('/<int:pk>/selected_date', DateSelectionCreateView.as_view(), name='apartments_selected_date'),
    path('/<int:pk>/comment_apartment', CommentApartmentAddView.as_view(), name='apartments_comment_apartment_add'),
    path('/photo_rooms/<int:pk>', PhotoRoomsDeletedView.as_view(), name='apartment_photo_rooms_delete'),

]
