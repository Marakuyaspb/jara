from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from django.urls import reverse

from .views import custom_404_view, custom_500_view



app_name = 'main'



urlpatterns = [

    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('ventilation/', views.ventilation, name = 'ventilation'),
    path('feedback/', views.feedback, name = 'feedback'),
    path('action/', views.action, name = 'action'),

]


handler404 = 'main.views.custom_404_view'
handler500 = 'main.views.custom_500_view'