# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from proveedores.models import Proveedor
from titulares.models import  Titular
from agentes.models import Agente


FPAGOS_CHOICES = [
    ["PAGARE", "Pagare"],
    ["TRANSFERENCIA", "Transferencia"],
]


class Producto(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    variedad = models.CharField(max_length=40,blank=True)
    kilos = models.IntegerField(null=True, blank=True, default=0)


    def __str__(self):
        return self.descripcion


class Compra(models.Model):
    titular = models.ForeignKey(Titular, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, null=True, blank=True)
    forma_pago = models.CharField(max_length=50, choices=FPAGOS_CHOICES, default="TRANSFERENCIA", verbose_name="Forma de Pago")
    fecha = models.DateField(auto_now_add=True)

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=7,decimal_places=2)
    fecha = models.DateField(auto_now_add=True)



