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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)