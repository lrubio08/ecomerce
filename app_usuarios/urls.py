from django.urls import path
from . import views 

urlpatterns = [
    path("registro/", views.registro, name="registro"),
    path("login/", views.login_views, name="login"),
    path("correo/", views.correo, name="correo"),
    path("recuperar_password/", views.recuperar_password, name="recuperar_password"),
    path("perfil_usuario/", views.perfil_usuario, name="perfil_usuario"),
    path("actualizar_datos/", views.actualizar_datos, name="actualizar_datos"),
]