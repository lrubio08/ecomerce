from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[('smartphone', 'Smartphone'), ('notebook', 'Notebook'), ('tablet', 'Tablet'), ('televisores', 'Televisores'), ('pc escritorio', 'PC Escritorio')])
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/')
    destacado = models.BooleanField(default=False)
    class Meta:
        abstract = True
    

class Smartphone(Producto):
    sistema_operativo = models.CharField(max_length=50)
    pantalla = models.CharField(max_length=50)  # Ej: "6.5'' AMOLED"
    camara_principal = models.CharField(max_length=50)  # Ej: "64 MP"
    camara_frontal = models.CharField(max_length=50)
    bateria = models.CharField(max_length=50)  # Ej: "5000 mAh"
    memoria_ram = models.CharField(max_length=20)
    almacenamiento = models.CharField(max_length=20)
    dual_sim = models.BooleanField(default=False)

class Notebook(Producto):
    procesador = models.CharField(max_length=50)
    memoria_ram = models.CharField(max_length=20)
    almacenamiento = models.CharField(max_length=20)
    tarjeta_grafica = models.CharField(max_length=50, blank=True)
    pantalla = models.CharField(max_length=50)
    sistema_operativo = models.CharField(max_length=50)
    peso = models.CharField(max_length=20)
    autonomia_bateria = models.CharField(max_length=50)

class Tablet(Producto):
    sistema_operativo = models.CharField(max_length=50)
    pantalla = models.CharField(max_length=50)
    memoria_ram = models.CharField(max_length=20)
    almacenamiento = models.CharField(max_length=20)
    camara_frontal = models.CharField(max_length=50)
    camara_trasera = models.CharField(max_length=50)
    conectividad = models.CharField(max_length=50)  # Ej: "WiFi + LTE"
    stylus_incluido = models.BooleanField(default=False)

class PcEscritorio(Producto):
    procesador = models.CharField(max_length=50)
    memoria_ram = models.CharField(max_length=20)
    almacenamiento = models.CharField(max_length=20)
    tarjeta_grafica = models.CharField(max_length=50)
    fuente_poder = models.CharField(max_length=50)
    gabinete = models.CharField(max_length=50)
    sistema_operativo = models.CharField(max_length=50)
    incluye_monitor = models.BooleanField(default=False)

class Televisor(Producto):
    tipo_pantalla = models.CharField(max_length=50)  # Ej: "LED", "OLED", "QLED"
    resolucion = models.CharField(max_length=50)     # Ej: "4K UHD", "Full HD"
    tamaño_pantalla = models.CharField(max_length=20) # Ej: "55 pulgadas"
    sistema_operativo = models.CharField(max_length=50)  # Ej: "webOS", "Android TV"
    smart_tv = models.BooleanField(default=True)
    puertos_hdmi = models.PositiveIntegerField()
    puertos_usb = models.PositiveIntegerField()
    conectividad = models.CharField(max_length=100)  # Ej: "WiFi, Bluetooth, Ethernet"
    sonido = models.CharField(max_length=100, blank=True)  # Ej: "Dolby Atmos"

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

class Filtro(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class OpcionFiltro(models.Model):
    filtro = models.ForeignKey(Filtro, on_delete=models.CASCADE)
    valor = models.CharField(max_length=50)
