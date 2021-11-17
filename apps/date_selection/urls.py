from django.urls import path

from .views import DateSelectionCreateView, DateSelectionRetrieveUpdateDestroyView
urlpatterns = [
    path('', DateSelectionCreateView.as_view(), name='date_selection_post'),
    path('/<int:pk>', DateSelectionRetrieveUpdateDestroyView.as_view(), name='date_selection_get_patch_put_delete')
    ]