from django.contrib import admin
from .models import Producto, Categoria, Filtro, OpcionFiltro, ValorAtributo, AtributoProducto, CategoriaAtributo


class OpcionFiltroInline(admin.TabularInline):
    model = OpcionFiltro
    extra = 2


class ValorAtributoInline(admin.TabularInline):
    model = ValorAtributo
    extra = 12   # una fila por atributo; ajústalo si quieres menos


@admin.register(Filtro)
class FiltroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
    inlines = [OpcionFiltroInline]
    search_fields = ('nombre',)
    list_filter = ('categoria',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock','marca')
    list_filter = ('categoria',)
    search_fields = ('nombre',)
    inlines = [ValorAtributoInline]


admin.site.register(OpcionFiltro)


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