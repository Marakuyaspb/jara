from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views
from django.urls import reverse

app_name = 'portfolio'


urlpatterns = [
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('<int:id>/', views.the_case, name='the_case'),
]