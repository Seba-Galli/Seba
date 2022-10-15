
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', lambda req: redirect('MiAppInicio')),
    path('admin/', admin.site.urls),
    path('AppBlogs/', include ('AppBlogs.urls')),
    path('UserBlog/', include ('UserBlog.urls')),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)