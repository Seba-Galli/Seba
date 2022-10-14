
from datetime import date, datetime
from distutils.command import *
from django.db import models
from ckeditor.fields import RichTextField
from tkinter import *
from tkcalendar import *

class Blogs(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto_corto = models.CharField(max_length=40)
    texto_largo = models.CharField(max_length=80)
    autor = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    
class Busqueda(models.Model):
    nombre_libro = models.CharField(max_length=20)
    nombre_autor = models.CharField(max_length=20)
    nombre_editorial = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=80)

    def __str__(self):
        return f"Libro: {self.nombre_libro}"

class BusquedaFiltrada(models.Model):
    nombre_libro = models.CharField(max_length=20)
    nombre_autor = RichTextField(max_length=400)
    imagen = models.ImageField(upload_to="imagenes", null=True)
    fecha = models.DateTimeField (default = datetime.now, blank = True)

class Musica(models.Model):
    cancion = models.CharField(max_length=20)
    album = models.CharField(max_length=20)
    artista = models.CharField(max_length=20)
    comentarios = models.CharField(max_length=80)
    premios = models.CharField(max_length=40)

class Futbol(models.Model):
    jugador = models.CharField(max_length=20)
    equipo = models.CharField(max_length=20)
    titulos = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=20)
