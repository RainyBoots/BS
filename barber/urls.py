from django.contrib import admin
from django.urls import path
from barbercut.views import main, thanks, ServiceFetchView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('thanks/', thanks, name='thanks'),
    path('fetch-services/', ServiceFetchView.as_view(), name='fetch_services')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)