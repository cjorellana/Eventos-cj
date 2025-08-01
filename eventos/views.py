from django.shortcuts import render, redirect, get_object_or_404
from .forms import contactoForm
from .models import evento, contacto
from django.contrib import messages
from datetime import date
from django.http import JsonResponse

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

        if not nombre_form or not email_form or not mensaje_form:
            messages.error(request, 'Todos los campos son obligatorios.')
        else:
            # Validar el formato del correo electrónico
            try:
                nuevo_contacto = contacto(nombre_persona=nombre_form, correo=email_form, mensaje=mensaje_form, tipo=1)  # Asignando un tipo por defecto
                nuevo_contacto.save()
                messages.success(request, 'Contacto guardado correctamente.')
            except Exception as e:
                messages.error(request, f'Error al guardar el contacto: {e}')

    return render(request, 'contacto.html')


def contacto2(request):
    if request.method == 'POST':
        nombre_form = request.POST.get('nombre', '')
        email_form = request.POST.get('email', '')
        mensaje_form = request.POST.get('mensaje', '')

        if not nombre_form or not email_form or not mensaje_form:
            messages.error(request, 'Todos los campos son obligatorios.')
        else:
            # Validar el formato del correo electrónico
            try:
                nuevo_contacto = contacto(nombre_persona=nombre_form, correo=email_form, mensaje=mensaje_form, tipo=1)  # Asignando un tipo por defecto
                nuevo_contacto.save()
                messages.success(request, 'Contacto guardado correctamente.')
            except Exception as e:
                messages.error(request, f'Error al guardar el contacto: {e}')

    return render(request, 'contacto2.html')

def contacto3(request):
    data = {
        'form': contactoForm(),
    }
       #metodo
    if request.method == 'POST':
        formulario= contactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Soporte Enviado Correctamente. ')
        else:
            messages.error(request,'Error al enviar el formulario')
            data['form']=formulario
    return render(request, 'contacto3.html', data)


def nuevo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        precio = request.POST.get('precio', '')
        fecha_inicio = request.POST.get('fecha_inicio', '')
        fecha_fin = request.POST.get('fecha_fin', '')
        fecha_Asig = request.POST.get('fecha_asignacion', '')
        fecha_fin_asig = request.POST.get('fecha_fin_de_asignacion', '')
        activo = request.POST.get('activo') == 'True'
        diploma = request.POST.get('diploma') == 'True'
        description = request.POST.get('descripcion', '')
        imagen = request.FILES.get('imagen', None)

        try:
            nuevo_evento = evento(
                nombre=nombre,
                precio=precio,
                description=description,
                fecha_Inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                fecha_Asig=fecha_Asig,
                fecha_fin_asig=fecha_fin_asig,
                activo=activo,
                diploma=diploma,
                image=imagen 
            )
            nuevo_evento.save()
            messages.success(request, 'Evento creado correctamente.')
            return redirect('nuevo')
        except Exception as e:
            messages.error(request, f'Error al crear el evento: {e}')
    return render(request, 'nuevo.html')

def listado(request):

    listado_eventos = evento.objects.all().order_by('fecha_Inicio')

    data = {
        
        'title': 'Listado de Eventos',
        'listado': listado_eventos,
    }

    return render(request, 'listado.html', data)

def api(request):

    eventos = evento.objects.all()
    # listado_eventos = list(eventos.values('id', 'nombre', 'precio', 'fecha_Inicio', 'fecha_fin', 'activo', 'diploma'))

    return JsonResponse(list(eventos.values()), safe=False)  
    # return JsonResponse({'eventos' : listado_eventos }, safe=False)  


def listado2(request):
    return render(request, 'listado2.html')

def pizza(request):
    return render(request, 'pizza.html')
