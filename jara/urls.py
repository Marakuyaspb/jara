from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

from main import urls
from catalog import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('', include('main.urls')),
    path('', include('portfolio.urls')),
]


urlpatterns += static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)