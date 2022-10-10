from django.urls import path
from AppBlogs.views import *

urlpatterns = [
    path('', inicio, name='MiAppInicio'),
    path('buscar_formulario/', buscar_formulario, name='AppBusquedaForm'),
    path('busqueda_libro_post/', busqueda_libro_post, name='AppBusquedaLibro'),
    path('cargar_formulario/', cargar_formulario, name='AppCargarForm'),
    path('cargadas/', cargadas, name='AppCargar'),
    path('eliminar_autor/<nombre_autor>', eliminar_autor, name='AppEliminarAutor'),
    path('editar_libro/<nombre_libro>', editar, name="AppEditarLibro")
]