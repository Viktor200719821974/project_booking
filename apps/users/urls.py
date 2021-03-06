from django.urls import path

from .views import UsersListCreateView, UserRetrieveUpdateDestroyView, UserToManagerView, UserBlockedView,\
    CommentUserAddView


urlpatterns = [
    path('', UsersListCreateView.as_view(), name='users_getAll_post'),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='user_get_patch_put_delete'),
    path('/<int:pk>/manager', UserToManagerView.as_view(), name='users_manager'),
    path('/<int:pk>/blocked', UserBlockedView.as_view(), name='users_blocked_user'),
    path('/<int:pk>/comment_user', CommentUserAddView.as_view(), name='users_comment_user_add')
   ]
