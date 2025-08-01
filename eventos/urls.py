from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [ # URL patterns de la aplicación eventos
    path('', views.home, name='home'),
    path('detalle/<int:id>', views.detalle, name='detalle'), # Detalle de un evento en particular 
    path('about/', views.about, name='about'),
    path('buscar/', views.buscar, name='buscar'),
    path('contacto/', views.Contacto, name='contacto'), 
    path('contacto2/', views.contacto2, name='contacto2'), 
    path('contacto3/', views.contacto3, name='contacto3'),    
    path('nuevo/', views.nuevo, name='nuevo'),                 
    path('listado/', views.listado, name='listado'),  # Listado de eventos
    path('api/eventos', views.api, name='api'),       
    path('listado2/', views.listado2, name='listado2'),  # Listado de eventos 2
    path('pizza/', views.pizza, name='pizza'),  # Página de pizza
    path('listadovue/', views.listadovue, name='listadovue'),  # Página de listado Vue



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)