from django.db import models
from django.utils.text import slugify


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    imagen_banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class AtributoProducto(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=[
        ('texto', 'Texto'),
        ('numero', 'Número'),
        ('rango', 'Rango'),
        ('booleano', 'Booleano'),
    ])
    unidad = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return self.nombre

class CategoriaAtributo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    atributo = models.ForeignKey(AtributoProducto, on_delete=models.CASCADE)
    es_filtrable = models.BooleanField(default=True)
    orden = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ('categoria', 'atributo')

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[('smartphone', 'Smartphone'), ('notebook', 'Notebook'), ('tablet', 'Tablet'), ('televisores', 'Televisores'), ('pc_escritorio', 'PC Escritorio')])
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/')
    destacado = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

class ValorAtributo(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='atributos')
    atributo = models.ForeignKey(AtributoProducto, on_delete=models.CASCADE)
    valor = models.CharField(max_length=200)
    
    class Meta:
        unique_together = ('producto', 'atributo')
        verbose_name = "Valor de Atributo"
        verbose_name_plural = "Valores de Atributos"
    
    def __str__(self):
        return f"{self.producto.nombre} - {self.atributo.nombre}: {self.valor}"
        

class Filtro(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
            return self.nombre


class OpcionFiltro(models.Model):
    filtro = models.ForeignKey(Filtro, on_delete=models.CASCADE)
    valor = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.filtro.nombre}: {self.valor}"

