from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalog import views
from django.urls import reverse

app_name = 'catalog'


urlpatterns = [
    path('catalog/', views.catalog, name = 'catalog'),
    path('<int:id>/', views.the_product, name='the_product'),
]