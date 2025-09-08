# app_productos/management/commands/setup_filtros.py
from django.core.management.base import BaseCommand
from app_productos.models import Categoria, AtributoProducto, CategoriaAtributo

class Command(BaseCommand):
    help = 'Configura atributos y filtros iniciales'
    
    def handle(self, *args, **options):
        self.stdout.write('Configurando atributos y filtros...')

        atributos = [
            ('marca', 'texto', ''),
            ('modelo', 'texto', ''),
            ('pantalla', 'rango', 'pulgadas'),
            ('almacenamiento', 'rango', 'GB'),
            ('ram', 'rango', 'GB'),
            ('bateria', 'rango', 'mAh'),
            ('sistema_operativo', 'texto', ''),
            ('procesador', 'texto', ''),
            ('camara', 'rango', 'MP'),
        ]
        
        for nombre, tipo, unidad in atributos:
            attr, created = AtributoProducto.objects.get_or_create(
                nombre=nombre,
                defaults={
                    'tipo': tipo,
                    'unidad': unidad
                }
            )
            if created:
                self.stdout.write(f'✓ Creado atributo: {nombre}')

        try:
            categoria_smartphone = Categoria.objects.get(slug='smartphone')
            atributos_smartphone = [
                'marca', 'modelo', 'pantalla', 'almacenamiento', 
                'ram', 'bateria', 'sistema_operativo', 'camara'
            ]
            
            for i, attr_nombre in enumerate(atributos_smartphone):
                attr = AtributoProducto.objects.get(nombre=attr_nombre)
                cat_attr, created = CategoriaAtributo.objects.get_or_create(
                    categoria=categoria_smartphone,
                    atributo=attr,
                    defaults={'orden': i, 'es_filtrable': True}
                )
                if created:
                    self.stdout.write(f'✓ Configurado filtro {attr_nombre} para smartphones')
            
            self.stdout.write(
                self.style.SUCCESS('¡Filtros configurados exitosamente!')
            )
            
        except Categoria.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('Error: No existe la categoría "smartphone". Créala primero.')
            )