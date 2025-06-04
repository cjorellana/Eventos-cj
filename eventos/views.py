from django.shortcuts import render
from .models import evento
# Create your views here.

def home(request):

    # listado = evento.objects.all().order_by('fecha_Inicio')
    listado_eventos = evento.objects.all().filter(activo=True).order_by('fecha_Inicio')
    # listado_eventos = evento.objects.all()

    data = {
        'title': 'Eventos',
        'listado': listado_eventos,
    }

    # data = {
    #     'title': 'Eventos',
    #     'parrafo': 'bienvenido al sistema de eventos!',
    #     'eventos': [
    #         {'nombre': 'Concierto de Rock', 'fecha': '2023-10-01', 'lugar': 'Estadio Nacional'},
    #         {'nombre': 'Feria de Tecnología', 'fecha': '2023-10-15', 'lugar': 'Centro de Convenciones'},
    #         {'nombre': 'Festival de Cine', 'fecha': '2023-11-05', 'lugar': 'Cinepolis'},
    #     ]
    # }
    return render(request, 'home.html', data)

def about(request):
    return render(request, 'about.html')