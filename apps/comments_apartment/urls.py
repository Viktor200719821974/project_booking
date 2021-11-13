from django.urls import path

from .views import CommentsApartmentListCreateView, CommentsApartmentRetrieveUpdateDestroyView, PhotoCommentApartmentView

urlpatterns = [
    path('', CommentsApartmentListCreateView.as_view(), name='comments_apartment_getAll_post'),
    path('/<int:pk>', CommentsApartmentRetrieveUpdateDestroyView.as_view(),
         name='comments_apartment_get_patch_put_delete'),
    path('/<int:pk>/addPhoto', PhotoCommentApartmentView.as_view(), name='comments_apartment_add_photo')
]