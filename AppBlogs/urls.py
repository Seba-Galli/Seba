from django.urls import path
from AppBlogs.views import *

urlpatterns = [
    path('', inicio, name='MiAppInicio'),
    path('buscar_formulario/', buscar_formulario, name='AppBusquedaForm'),
    path('busquedas/', busquedas, name='AppBusquedas'),
    path('cargar_formulario/', cargar_formulario, name='AppCargarForm'),
    path('cargadas/', cargadas, name='AppCargar'),
    path('eliminar_libro/>', eliminar_libro, name='AppEliminarLibro'),
    path('editar_libro/>', editar, name="AppEditarLibro")
]