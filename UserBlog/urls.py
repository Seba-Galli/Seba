from django.urls import path
from UserBlog.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login_request, name='UserBlogLogin'),
    path('registro/', register, name='UserBlogRegistro'),
    path('logout/', LogoutView.as_view(template_name='UserBlog/logout.html'), name='UserBlogLogOut'),
    path('editar/', editar_usuario, name='UserBlogEditar'),
    path('avatar/', upload_avatar, name='UserBlogAvatar'),
]