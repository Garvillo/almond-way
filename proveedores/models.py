# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class EntidadCertificadora(models.Model):
    nombre=  models.CharField(max_length=150, verbose_name=" Organismo de Certificación y Control")
    Observaciones =models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    ruc = models.CharField(unique=True,max_length=11,verbose_name ="DNI/CIF")
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=15,null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    entidad_certificadora = models.ForeignKey(EntidadCertificadora,  on_delete=models.CASCADE, blank=True, null=True)
    observaciones_eco = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.razon_social