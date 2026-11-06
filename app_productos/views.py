
from django.shortcuts import get_object_or_404, render

from .models import (
    AtributoProducto,
    Categoria,
    CategoriaAtributo,
    Filtro,
    Producto,
    ValorAtributo,
)


def productos_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)

    # Todos los productos de la categoría (sin filtrar)
    productos_base = Producto.objects.filter(categoria=categoria, stock__gt=0)

    # Opciones del panel, calculadas con todos los productos
    filtros_dinamicos = generar_filtros_dinamicos(categoria, productos_base)

    # Productos ya filtrados según lo que se marcó
    resultado = aplicar_filtros(request, productos_base)

    contexto = {
        'titulo': f'{categoria.nombre}: variedad, tecnología y estilo',
        'imagen_banner': categoria.imagen_banner.url if categoria.imagen_banner else None,
        'productos': resultado['productos'],
        'categoria': categoria,
        'filtros': Filtro.objects.filter(categoria=categoria),  # sistema viejo, lo quitamos después
        'filtros_dinamicos': filtros_dinamicos,
        'filtros_aplicados': resultado['aplicados'],
        'tipo_submenu': 'filtros',
    }

    return render(request, 'app_productos/productos_categorias.html', contexto)


def generar_filtros_dinamicos(categoria, productos):
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

    for key in request.GET:
        if not key.startswith('filtro_'):
            continue
        valores = [v for v in request.GET.getlist(key) if v]
        if not valores:
            continue

        nombre = key.replace('filtro_', '', 1)

        if nombre == 'precio':
            try:
                precio_min, precio_max = valores[0].split('-')
                productos = productos.filter(precio__gte=precio_min, precio__lte=precio_max)
            except ValueError:
                continue
        else:
            productos = productos.filter(
                atributos__atributo__nombre=nombre,
                atributos__valor__in=valores
            )

        filtros_aplicados[nombre] = valores

    return {'productos': productos.distinct(), 'aplicados': filtros_aplicados}

def detalle_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    # Valores de atributos del producto (RAM, pantalla, etc.)
    orden = dict(
        CategoriaAtributo.objects
        .filter(categoria=producto.categoria)
        .values_list('atributo_id', 'orden')
    )
    especificaciones = sorted(
        producto.atributos.select_related('atributo'),
        key=lambda v: orden.get(v.atributo_id, 999),
    )

    # Otros productos de la misma categoría
    relacionados = (
        Producto.objects
        .filter(categoria=producto.categoria, stock__gt=0)
        .exclude(pk=producto.pk)[:4]
    )

    return render(request, 'app_productos/detalle_productos.html', {
        'producto': producto,
        'especificaciones': especificaciones,
        'relacionados': relacionados,
    })
