from django.contrib import admin
from django.urls import path
from barbercut.views import MainView, ThanksTemplateView, VisitCreateView, VisitDetailView, VisitUpdateView, VisitDeleteView, ServicesByMasterView
from django.conf.urls.static import static
from django.conf import settings
from users import urls
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", MainView.as_view(), name="main"),
    path("thanks/", ThanksTemplateView.as_view(), name="thanks"),
    path(
        "get_services_by_master/<int:master_id>/",
        ServicesByMasterView.as_view(),
        name="get_services_by_master",
    ),
    path("visit/add/", VisitCreateView.as_view(), name="visit-form"),
    path("visit/<int:pk>/view/", VisitDetailView.as_view(), name="visit-view"),
    path("visit/<int:pk>/edit/", VisitUpdateView.as_view(), name="visit-edit"),
    path("visit/<int:pk>/delete/", VisitDeleteView.as_view(), name="visit-delete"),
    path("user/", include(urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)