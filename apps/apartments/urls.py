from django.urls import path

from .views import  ApartmentListCreateView, ApartmentRetrieveUpdateDestroyView, PhotoRoomsView

urlpatterns = [
    path('', ApartmentListCreateView.as_view()),
    path('/<int:pk>', ApartmentRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/photo_rooms', PhotoRoomsView.as_view())
]