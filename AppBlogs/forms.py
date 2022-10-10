from django import forms

class BusquedaForm(forms.Form):
    nombre_libro = forms.CharField(max_length=20)
    nombre_autor = forms.CharField(max_length=20)
    nombre_editorial = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=80)

class CargarForm(forms.Form):
    titulo = forms.CharField(max_length=20)
    subtitulo = forms.CharField(max_length=20)
    texto_corto = forms.CharField(max_length=40)
    texto_largo = forms.CharField(max_length=80)
    autor = forms.CharField(max_length=40)
    email = forms.CharField(max_length=40)

class BusquedaLibroForm(forms.Form):
    nombre_libro = forms.CharField(max_length=20)

class BusquedaLibroForm(forms.Form):
    nombre_libro = forms.CharField(max_length=20)
    nombre_autor = forms.CharField(max_length=20)
