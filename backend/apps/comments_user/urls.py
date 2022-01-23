from django.urls import path

from .views import CommentsUserListView, CommentsUserRetrieveUpdateDestroyView, PhotoCommentUserView, \
    PhotoCommentUserDeletedView

urlpatterns = [
    path('', CommentsUserListView.as_view(), name='comments_user_getAll'),
    path('/<int:pk>', CommentsUserRetrieveUpdateDestroyView.as_view(), name='comments_user_get_patch_put_delete'),
    path('/<int:pk>/addPhoto', PhotoCommentUserView.as_view(), name='comments_user_add_photo'),
    path('/deletePhoto/<int:pk>', PhotoCommentUserDeletedView.as_view(), name='comments_user_delete_photo'),

]
