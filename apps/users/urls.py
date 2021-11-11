from django.urls import path

from .views import UsersListCreateView, UserRetrieveUpdateDestroyView, UserToManagerView, UserBlockedView
    # UserAddApartmentView


urlpatterns = [
    path('', UsersListCreateView.as_view()),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/manager', UserToManagerView.as_view()),
    path('/<int:pk>/blocked', UserBlockedView.as_view()),
    # path('/<int:pk>/apartment', UserAddApartmentView.as_view())
   ]
