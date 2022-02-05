from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    #
    # # path to djoser end points
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

    # # path to our account's app endpoints
    # path("api/accounts/", include("users.urls"))
    path('api/v1', include('urls.api_v1'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)