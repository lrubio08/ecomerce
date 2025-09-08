from django.contrib import admin
from .models import Producto, Categoria, Filtro, OpcionFiltro, ValorAtributo, AtributoProducto, CategoriaAtributo

class OpcionFiltroInline(admin.TabularInline):
    model = OpcionFiltro
    extra = 2

@admin.register(Filtro)
class FiltroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')  # si tienes el campo 'categoria'
    inlines = [OpcionFiltroInline]
    search_fields = ('nombre',)
    list_filter = ('categoria',)

admin.site.register(Categoria)
admin.site.register(OpcionFiltro)
admin.site.register(Producto)  # ← Simple por ahora

class ValorAtributoInline(admin.TabularInline):
    model = ValorAtributo
    extra = 3

@admin.register(AtributoProducto)
class AtributoProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'unidad')
    search_fields = ('nombre',)

@admin.register(ValorAtributo)
class ValorAtributoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'atributo', 'valor')
    list_filter = ('atributo',)
    search_fields = ('producto__nombre', 'valor')

@admin.register(CategoriaAtributo)
class CategoriaAtributoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'atributo', 'es_filtrable', 'orden')
    list_filter = ('categoria',)