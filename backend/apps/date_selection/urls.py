from django.urls import path

from .views import DateSelectionDestroyView, YesRentView, NoRentView, DateSelectionListView
urlpatterns = [
    path('', DateSelectionListView.as_view(), name='date_selection_get_all'),
    path('/<int:pk>', DateSelectionDestroyView.as_view(), name='date_selection_get_patch_put_delete'),
    path('/yes/<str:token_yes>', YesRentView.as_view(), name='date_selection_yes'),
    path('/no/<str:token_no>', NoRentView.as_view(), name='date_selection_no')
    ]