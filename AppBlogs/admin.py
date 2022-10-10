from django.contrib import admin
from AppBlogs.models import Blogs, Busqueda, BusquedaFiltrada

admin.site.register(Blogs)
admin.site.register(Busqueda)
admin.site.register(BusquedaFiltrada)