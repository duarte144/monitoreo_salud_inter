

# Create your models here.



from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username


class Gato(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    raza = models.CharField(max_length=50, blank=True, null=True)
    peso = models.FloatField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class RegistroTemperatura(models.Model):
    gato = models.ForeignKey(Gato, on_delete=models.CASCADE)
    temperatura = models.FloatField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.gato.nombre} - {self.temperatura}°C ({self.fecha_registro})"

