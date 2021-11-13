from django.urls import path

from .views import DateSelectionCreateView
urlpatterns = [
    path('/<int:pk>', DateSelectionCreateView.as_view(), name='date_selection_post')
    ]