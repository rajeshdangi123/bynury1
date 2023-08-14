from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.base, name="base"),
    path("create_request", views.create_request, name="create_request"),
    path("get/", views.get, name="get"),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
