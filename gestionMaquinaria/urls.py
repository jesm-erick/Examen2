from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include 
from gestionMaquinaria import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gestionMaquinaria/', include('gestionMaquinaria.urls')),
    url(r'^admin/', admin.site.urls),