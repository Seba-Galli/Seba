
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
import django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

def about(request):
    return render(request, 'Apps/about.html')


def editar(request, nombre_libro):
    libro_editar = BusquedaFiltrada.objects.get(nombre_libro=nombre_libro)

    if request.method == 'POST':
        mi_formulario = BusquedaLibroForm(request.POST, request.FILES)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            libro_editar.nombre_libro = data.get('nombre_libro')
            libro_editar.nombre_autor = data.get('nombre_autor')
            libro_editar.imagen = data.get('imagen')
            try:
                libro_editar.save()
            except django.db.utils.IntegrityError:
                messages.error(request, "la modificacion fallo por que el libro esta repetido")

            return redirect('AppBusqueda')

    contexto = {
        'form': BusquedaLibroForm(
            initial={
                "nombre_libro": libro_editar.nombre_libro,
                "nombre_autor": libro_editar.nombre_autor,
                "imagen": libro_editar.imagen,
            }
        ),
        'nombre_form': 'Formulario',
        'boton_envio': 'Crear'
    }

    return render(request, 'base_formulario.html', contexto)


def eliminar_autor(request, nombre_autor):
    autor_eliminar = BusquedaFiltrada.objects.get(nombre_autor=nombre_autor)
    autor_eliminar.delete()

    messages.info(request, f"El autor {nombre_autor} fue eliminado")

    return redirect('AppBusqueda')

@login_required
def buscar_formulario(request):

    if request.method == "POST":
        mi_formulario = BusquedaLibroForm(request.POST, request.FILES)

        if mi_formulario.is_valid():
        
            data = mi_formulario.cleaned_data

            buscar = BusquedaFiltrada(nombre_libro=data.get('nombre_libro'), nombre_autor=data.get('nombre_autor'), imagen=data.get('imagen'), fecha=data.get('fecha'))
            
            buscar.save()

            return redirect('AppBusqueda')

    contexto = {
        'form': BusquedaLibroForm(),
        'nombre_form': 'Buscar Libro',
        'boton_envio': 'Buscar'
    }

    return render(request, "base_formulario.html", contexto)

@login_required
def busqueda(request):

    contexto = {
        'form': BusquedaLibroForm(),
        'nombre_form': 'Buscar Libro',
        'boton_envio': 'Buscar'
    }

    return render(request, 'Apps/busqueda.html', contexto)

@login_required
def cargar_formulario(request):

    if request.method == "POST":
        mi_formulario = BusquedaLibroForm(request.POST, request.FILES)

        if mi_formulario.is_valid():
        
            data = mi_formulario.cleaned_data

            libro = BusquedaFiltrada(nombre_libro=data.get('nombre_libro'), nombre_autor=data.get('nombre_autor'), imagen=data.get('imagen'))
            
            libro.save()

            return redirect('AppCargarForm')
            

    contexto = {
        'form': BusquedaLibroForm(),
        'nombre_form': 'Cargar Libro',
        'boton_envio': 'Crear'
    }

    return render(request, "base_formulario.html", contexto)


def inicio(request):
    return render(request, 'index.html')


class CargarList(LoginRequiredMixin, ListView):
    model = BusquedaFiltrada
    template_name = 'Apps/cargar.html'

@login_required
def cargadas(request):

    cargar = BusquedaFiltrada.objects.all()
            
    contexto = {
        'object_list': cargar
    }

    return render(request,"Apps/cargar.html", contexto)

