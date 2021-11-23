from django.urls import path

from .views import DateSelectionDestroyView, YesRentView
urlpatterns = [
    path('/<int:pk>', DateSelectionDestroyView.as_view(), name='date_selection_get_patch_put_delete'),
    path('/yes/<str:token>', YesRentView.as_view(), name='apartment_yes')
    ]