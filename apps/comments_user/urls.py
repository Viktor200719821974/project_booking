from django.urls import path

from .views import CommentsUserListCreateView, CommentsUserRetrieveUpdateDestroyView

urlpatterns = [
    path('', CommentsUserListCreateView.as_view()),
    path('<int:pk>', CommentsUserRetrieveUpdateDestroyView.as_view()),
]