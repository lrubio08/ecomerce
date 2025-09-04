from django.urls import path
from . import views 

urlpatterns = [
    path("registro/", views.registro, name="registro"),
    path("login/", views.login_views, name="login"),
    path("logout/", views.logout, name="logout"),
    path('correo_recuperacion_password/', views.correo_recuperacion_password, name='correo_recuperacion_password'),
    path('recuperar_password/<uidb64>/<token>/', views.recuperar_password, name='recuperar_password'),
    path("perfil_usuario/", views.perfil_usuario, name="perfil_usuario"),
    path("actualizar_datos/", views.actualizar_datos, name="actualizar_datos"),
]