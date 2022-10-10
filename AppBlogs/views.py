
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
import django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


def editar(request, nombre_libro):
    libro_editar = BusquedaFiltrada.objects.get(nombre_libro=nombre_libro)

    if request.method == 'POST':
        mi_formulario = BusquedaLibroForm(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            libro_editar.nombre_libro = data.get('nombre_libro')
            libro_editar.nombre_autor = data.get('nombre_autor')
            try:
                libro_editar.save()
            except django.db.utils.IntegrityError:
                messages.error(request, "la modificacion fallo por que el libro esta repedito")

            return redirect('AppCargar')

    contexto = {
        'form': BusquedaLibroForm(
            initial={
                "nombre_libro": libro_editar.nombre_libro,
                "nombre_autor": libro_editar.nombre_autor,
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

    return redirect("AppCargar")


def busqueda_libro_post(request):

    nombre_libro = request.GET.get('nombre_libro')

    buscar = BusquedaFiltrada.objects.filter(nombre_libro__icontains=nombre_libro)

    contexto = {
        'buscar': buscar
     }

    return render(request, "Apps/busqueda.html", contexto)

@login_required
def buscar_formulario(request):

    contexto = {
        'form': BusquedaLibroForm(),
        'nombre_form': 'Buscar Libro',
        'boton_envio': 'Buscar'
    }

    return render(request, 'Apps/busqueda_libro.html', contexto)

@login_required
def cargar_formulario(request):

    if request.method == "POST":
        mi_formulario = BusquedaLibroForm(request.POST)

        if mi_formulario.is_valid():
        
            data = mi_formulario.cleaned_data

            libro = BusquedaFiltrada(nombre_libro=data.get('nombre_libro'), nombre_autor=data.get('nombre_autor'))
            
            libro.save()

            return redirect('AppCargar')

    contexto = {
        'form': BusquedaLibroForm(),
        'titulo_form': 'Cargar Libro',
        'boton_envio': 'Crear'
    }

    return render(request, "base_formulario.html", contexto)


def inicio(request):
    return render(request, 'index.html')


class CargarList(LoginRequiredMixin, ListView):
    model = BusquedaFiltrada
    template_name = 'Apps/cargar.html'


def cargadas(request):

    cargar = BusquedaFiltrada.objects.all()
            
    contexto = {
        'object_list': cargar
    }

    return render(request,"Apps/cargar.html", contexto)

