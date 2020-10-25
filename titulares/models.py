from django.db import models

TIPOS_CHOICES = [
    ["COMPRAS", "Compras"],
    ["VENTAS", "Ventas"],
]

class Titular(models.Model):
    nombre = models.CharField(max_length=150)
    letra = models.CharField(max_length=2, default="A")
    cif = models.CharField(unique=True, max_length=11)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=15,null=True, blank=True)
    correo = models.EmailField( null=True, blank=True)
    activo = models.BooleanField(default=True)

    disponible_para = models.CharField(max_length=50, choices=TIPOS_CHOICES, default="COMPRAS",
                                  verbose_name="indica si este titular esta disponible para compras o ventas")

    def __str__(self):
        return self.nombre
