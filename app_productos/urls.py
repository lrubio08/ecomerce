from django.urls import path
from . import views 

urlpatterns = [
    path('categoria/<slug:slug>/', views.productos_por_categoria, name='productos_por_categoria'),

]