from django.shortcuts import render, redirect, get_object_or_404

from .models import evento, contacto
# Create your views here.

def home(request):

    # listado = evento.objects.all().order_by('fecha_Inicio') 
    # listado_eventos = evento.objects.all().filter(activo=True).order_by('fecha_Inicio')
    listado_eventos = evento.objects.all()

    data = {
        'title': 'Eventos Galileo',
        'listado': listado_eventos,
    }
    
    return render(request, 'home.html', data)

def about(request):

    return render(request, 'about.html')




def buscar(request):
    nombre = request.POST.get('nombre', '')

    if nombre:
        listado_eventos = evento.objects.filter(nombre__icontains=nombre).order_by('fecha_Inicio')
    else:
        listado_eventos = evento.objects.all().order_by('fecha_Inicio')
    data = {
        'title': 'Eventos encontrados...',
        'listado': listado_eventos,
    }
    return render(request, 'home.html', data)

def detalle(request, id=None):
    if id is None:
        return redirect('home')

    listado_eventos = get_object_or_404(evento, pk=id) 

    data = {
        'title': 'Detalle del evento',
        'listado': listado_eventos,
    }

    return render(request, 'detalle.html', data)

def Contacto(request):
    if request.method == 'POST':
        nombre_form = request.POST.get('nombre', '')
        email_form = request.POST.get('email', '')
        mensaje_form = request.POST.get('mensaje', '')

        nuevo_contacto = contacto(nombre_persona=nombre_form, correo=email_form, mensaje=mensaje_form, tipo=1)  # Asignando un tipo por defecto
        nuevo_contacto.save()
    return render(request, 'contacto.html')


