
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
import django

def editar(request, nombre_libro):
    libro_editar = Busqueda.objects.get(nombre_libro=nombre_libro)

    if request.method == 'POST':
        mi_formulario = BusquedaLibroForm(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            libro_editar.nombre_libro = data.get('nombre_libro')
            try:
                libro_editar.save()
            except django.db.utils.IntegrityError:
                messages.error(request, "la modificacion fallo por que el libro esta repedito")

            return redirect('AppCargar')

    contexto = {
        'form': BusquedaLibroForm(
            initial={
                "nombre": libro_editar.nombre_libro,
            }
        ),
        'titulo_form': 'Formulario',
        'boton_envio': 'Crear'
    }

    return render(request, 'base_formulario.html', contexto)

def cargar_formulario(request):

    if request.method == "POST":
        mi_formulario = BusquedaForm(request.POST)

        if mi_formulario.is_valid():
        
            data = mi_formulario.cleaned_data

            cargar = Busqueda(nombre_libro=data.get('nombre_libro'), nombre_autor=data.get('nombre_autor'), nombre_editorial=data.get('nombre_editorial'), descripcion=data.get('descripcion'))
            
            cargar.save()

            return redirect('AppCargar')

    contexto = {
        'form': BusquedaForm(),
        'titulo_form': 'Cargar Libro Formulario',
        'boton_envio': 'Crear'
    }

    return render(request, "base_formulario.html", contexto)

def eliminar_libro(request, nombre_libro):
    libro_eliminar = Busqueda.objects.get(nombre_libro=nombre_libro)
    libro_eliminar.delete()

    messages.info(request, f"El libro {libro_eliminar} fue eliminado")

    return redirect("AppCargar")

def cargadas(request):

    cargar = Busqueda.objects.all()
            
    contexto = {
        'object_list': cargar
    }

    return render(request,"Apps/cargar.html", contexto)


def buscar_formulario(request):

    buscar = Busqueda.objects.all()
     
    contexto = {
        'buscar': buscar
    }

    return render(request,"Apps/buscar_form.html", contexto)

def busquedas(request):

        nombre_libro = request.GET.get('nombre_libro')

        buscar = Busqueda.objects.filter(nombre_libro__icontains=nombre_libro)

        contexto = {
            'buscar': buscar
        }

        return render(request, "Apps/busqueda.html", contexto)


def inicio(request):
    return render(request, 'index.html')
