from django.db import models

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