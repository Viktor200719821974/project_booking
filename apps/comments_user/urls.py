from django.urls import path

from .views import CommentsUserListCreateView, CommentsUserRetrieveUpdateDestroyView, PhotoCommentUserView

urlpatterns = [
    path('', CommentsUserListCreateView.as_view(), name='comments_user_getAll_post'),
    path('/<int:pk>', CommentsUserRetrieveUpdateDestroyView.as_view(),name='comments_user_get_patch_put_delete'),
    path('/<int:pk>/addPhoto', PhotoCommentUserView.as_view(), name='comments_user_add_photo')
]