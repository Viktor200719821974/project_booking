from django.urls import path

from .views import CommentsApartmentRetrieveUpdateDestroyView, PhotoCommentApartmentView, CommentsApartmentListView, \
    PhotoCommentApartmentDeletedView

urlpatterns = [
    path('', CommentsApartmentListView.as_view(), name='comments_apartments_getAll'),
    path('/<int:pk>', CommentsApartmentRetrieveUpdateDestroyView.as_view(),
         name='comments_apartment_get_patch_put_delete'),
    path('/<int:pk>/addPhoto', PhotoCommentApartmentView.as_view(), name='comments_apartment_add_photo'),
    path('/deletePhoto/<int:pk>', PhotoCommentApartmentDeletedView.as_view(), name='comments_apartment_delete_photo'),

]
