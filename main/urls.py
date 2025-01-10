from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from django.urls import reverse

from .views import custom_404_view, custom_500_view



app_name = 'main'


urlpatterns = [

    path('', views.index, name = 'index'),
    path('contact/', views.contact, name = 'contact'),
    path('feedback/', views.feedback, name = 'feedback'),    
    path('install/', views.install, name = 'install'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('service/', views.service, name = 'service'),
    path('stock/', views.stock, name = 'stock'),
    path('ventilation/', views.ventilation, name = 'ventilation'),
    path('privacy/', views.privacy, name = 'privacy'),
    
]


handler404 = 'main.views.custom_404_view'
handler500 = 'main.views.custom_500_view'