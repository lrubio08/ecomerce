from django.urls import path

from . import views

urlpatterns = [
    path('categoria/<slug:slug>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('detalle_productos/<int:pk>/', views.detalle_productos, name= 'detalle_productos' )
]