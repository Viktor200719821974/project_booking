from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('api/v1', include('urls.api_v1'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)