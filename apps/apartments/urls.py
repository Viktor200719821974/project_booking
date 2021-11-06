from django.urls import path

from .views import  ApartmentListCreateView, ApartmentRetrieveUpdateDestroyView

urlpatterns = [
    path('', ApartmentListCreateView.as_view()),
    path('/<int:pk>', ApartmentRetrieveUpdateDestroyView.as_view())
]