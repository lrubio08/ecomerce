from django.shortcuts import render
from app_productos.models import Categoria


# Vista para el index global
def index(request):
    categorias = Categoria.objects.all()
    return render(request, "index.html", {
        "categorias": categorias,
        "tipo_submenu": "categorias"
    })

