# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from proveedores.models import Proveedor
from titulares.models import  Titular
from agentes.models import Agente
from clientes.models import Cliente
from django_extensions.db.models import TimeStampedModel
#from pagares.models import PagareCompra, PagareVenta


FPAGOS_CHOICES = [
    ["PAGARE", "Pagare"],
    ["TRANSFERENCIA", "Transferencia"],
]
SE_CALCULA_CON = [
    ["BASE", "Base"],
    ["TOTAL", "Total"],
]

class Producto(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    variedad = models.CharField(max_length=40,blank=True)
    kilos = models.IntegerField(null=True, blank=True, default=0)
    lote = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.descripcion
class Impuestos(models.Model):

    nombre = models.CharField(max_length=150)
    impuesto1 = models.IntegerField()
    impuesto2 = models.IntegerField(null=True, blank=True,)
    se_calcula_con = models.CharField(max_length=50, choices=SE_CALCULA_CON, default="BASE", null=True, blank=True, verbose_name="Valor con el que se calcula impuesto 2")

    def __str__(self):
        return self.nombre

# COMPRA -------------------------------------------------------------------------------

class Compra(TimeStampedModel):
    titular = models.ForeignKey(Titular, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, null=True, blank=True)
    forma_pago = models.CharField(max_length=50, choices=FPAGOS_CHOICES, default="TRANSFERENCIA", verbose_name="Forma de Pago")
    fecha = models.DateField(auto_now_add=True)

    nfact = models.IntegerField()
    lfact = models.CharField(max_length=2)

    impuestos = models.ForeignKey(Impuestos, on_delete=models.CASCADE)
    imp_aplicado = models.DecimalField(null=True, blank = True, decimal_places=2, max_digits=12)
    base = models.DecimalField(null=True, blank=True,decimal_places=2, max_digits=12)
    total = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=12)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "{}{} {}".format(self.lfact, str(self.nfact).zfill(5), self.proveedor)

    def numero(self):
        return "{}{}" .format(self.lfact, str(self.nfact).zfill(5))

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=7,decimal_places=2)

    fecha = models.DateField(auto_now_add=True)
    lote_heredado = models.CharField(max_length=40, blank=True, null=True)

# VENTAS ----------------------------------------------------------------------------

class Venta(models.Model):
    titular = models.ForeignKey(Titular, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, null=True, blank=True)
    forma_pago = models.CharField(max_length=50, choices=FPAGOS_CHOICES, default="TRANSFERENCIA", verbose_name="Forma de Pago")
    fecha = models.DateField(auto_now_add=True)

    nfact = models.IntegerField()
    lfact = models.CharField(max_length=2)

    impuestos = models.ForeignKey(Impuestos, on_delete=models.CASCADE)
    imp_aplicado = models.DecimalField(null=True, blank = True, decimal_places=2, max_digits=12)
    base = models.DecimalField(null=True, blank=True,decimal_places=2, max_digits=12)
    total = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=12)

    def __str__(self):
        return "{}{} {}".format(self.lfact, str(self.nfact).zfill(5), self.cliente)

    def numero(self):
        return "{}{}" .format(self.lfact, str(self.nfact).zfill(5))


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_venta = models.DecimalField(max_digits=7,decimal_places=2)

    fecha = models.DateField(auto_now_add=True)
    lote_heredado = models.CharField(max_length=40, blank=True, null=True)

class Historico(TimeStampedModel):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, blank=True, null=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, blank=True, null=True )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True)
    precio_venta = models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    lote_heredado = models.CharField(max_length=40, blank=True, null=True)
    kilos_actuales = models.IntegerField(null=True, blank=True)
