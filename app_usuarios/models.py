from django.db import models
from django.contrib.auth.models import AbstractUser

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Usuarios(AbstractUser):
    direccion = models.TextField(max_length=255, blank=True, null=True)
    comuna = models.TextField(max_length=255, blank=True, null=True)
    ciudad = models.TextField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    rut = models.CharField(max_length=12, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=10, blank=True, null=True, choices=[
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ])
    estado_cuenta = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    notificacion = models.BooleanField(default=False)
    TipoUsuario = models.ForeignKey(
        'TipoUsuario',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username 



