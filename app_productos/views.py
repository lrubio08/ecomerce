from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto, AtributoProducto, ValorAtributo
from django.db.models import Count, Q
from collections import defaultdict

# Create your views here.
from .models import Filtro

def productos_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    productos = Producto.objects.filter(categoria=categoria, stock__gt=0)

    filtros_aplicados = aplicar_filtros(request, productos)
    productos = filtros_aplicados['productos']

    filtros_disponibles = Filtro.objects.filter(categoria=categoria)

    contexto = {
        'titulo': f'{categoria.nombre}: variedad, tecnología y estilo',
        'imagen_banner': categoria.imagen_banner.url,
        'productos': productos,
        'categoria': categoria,
        'filtros': filtros_disponibles,
        'filtros_aplicados': filtros_aplicados['aplicados'],
        'tipo_submenu': 'filtros'
    }

    return render(request, 'app_productos/productos_categorias.html', contexto)


def generar_filtros_dinamicos(categoria, productos):
    """Genera filtros dinámicos basados en los productos disponibles"""
    filtros = {}

    atributos = AtributoProducto.objects.filter(
        categoriaatributo__categoria=categoria,
        categoriaatributo__es_filtrable=True
    ).order_by('categoriaatributo__orden')
    
    for atributo in atributos:
        valores = ValorAtributo.objects.filter(
            producto__in=productos,
            atributo=atributo
        ).values_list('valor', flat=True).distinct()
        
        if valores:
            if atributo.tipo == 'rango':
                valores_numericos = [int(v.split()[0]) for v in valores if v.split()[0].isdigit()]
                if valores_numericos:
                    filtros[atributo.nombre] = {
                        'tipo': 'rango',
                        'min': min(valores_numericos),
                        'max': max(valores_numericos),
                        'unidad': atributo.unidad
                    }
            else:
                filtros[atributo.nombre] = {
                    'tipo': 'lista',
                    'valores': list(valores)
                }

    precios = productos.values_list('precio', flat=True)
    if precios:
        filtros['precio'] = {
            'tipo': 'rango',
            'min': int(min(precios)),
            'max': int(max(precios)),
            'unidad': '$'
        }
    
    return filtros

def aplicar_filtros(request, productos_base):
    productos = productos_base
    filtros_aplicados = {}
    
    for key, value in request.GET.items():
        if key.startswith('filtro_') and value:
            atributo_nombre = key.replace('filtro_', '')
            
            if atributo_nombre == 'precio':
                precio_min, precio_max = value.split('-')
                productos = productos.filter(
                    precio__gte=precio_min,
                    precio__lte=precio_max
                )
            else:
                valores = value.split(',')
                productos = productos.filter(
                    atributos__atributo__nombre=atributo_nombre,
                    atributos__valor__in=valores
                )
            
            filtros_aplicados[atributo_nombre] = value
    
    return {
        'productos': productos.distinct(),
        'aplicados': filtros_aplicados
    }