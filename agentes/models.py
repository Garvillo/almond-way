from django.db import models


class Agente(models.Model):
    nombre = models.CharField(max_length=150)
    cif = models.CharField(unique=True, max_length=11, null=True, blank=True)
    observaciones = models.CharField(max_length=500, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=15,null=True, blank=True)
    correo = models.EmailField( null=True, blank=True)
    activo = models.BooleanField(default=True)


    def __str__(self):
        return self.nombre