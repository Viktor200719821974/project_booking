from django.urls import path

from .views import CommentsApartmentListCreateView, CommentsApartmentRetrieveUpdateDestroyView

urlpatterns = [
    path('', CommentsApartmentListCreateView.as_view()),
    path('<int:pk>', CommentsApartmentRetrieveUpdateDestroyView.as_view()),
]