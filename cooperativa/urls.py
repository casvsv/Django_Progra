
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', include('apps.cliente.urls'), name='cliente'),
    path('login/', include('apps.login.urls')),
    path('', views.homePage, name='home_page'),
]