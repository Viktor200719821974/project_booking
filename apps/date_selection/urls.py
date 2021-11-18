from django.urls import path

from .views import DateSelectionDestroyView
urlpatterns = [
    path('/<int:pk>', DateSelectionDestroyView.as_view(), name='date_selection_get_patch_put_delete')
    ]