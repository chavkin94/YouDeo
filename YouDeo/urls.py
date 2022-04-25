from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main.views import pageNotFound

urlpatterns = [
    #path('', include('women.urls')),
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('main', include('main.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = pageNotFound