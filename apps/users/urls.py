from django.urls import path

from .views import UsersListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('', UsersListCreateView.as_view()),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view()),
    # path('/<int:pk>/menager', UserToManagerView.as_view()),
    # path('/<int:pk>/blocked', UserBlockedView.as_view()),
    # path('/<int:pk>/apartment', UserAddApartmentView.as_view())
   ]
    # , UserToManagerView, UserBlockedView, \
    # UserAddApartmentView