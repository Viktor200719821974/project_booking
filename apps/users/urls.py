from django.urls import path

from .views import UsersListCreateView, UserRetrieveUpdateDestroyView, UserToMenagerView, UserBlockedView, \
    UserAddApartmentView

urlpatterns = [
    path('', UsersListCreateView.as_view()),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/menager', UserToMenagerView.as_view()),
    path('/<int:pk>/blocked', UserBlockedView.as_view()),
    path('/<int:pk>/apartment', UserAddApartmentView.as_view())
   ]