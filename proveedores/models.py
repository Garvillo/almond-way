# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CertificadoEco(models.Model):
    proveedor_certificado=  models.CharField(max_length=150)
    nombre  = models.CharField(max_length=150)
    fecha_inicio = models.DateField(auto_now_add=True, blank=True, null=True)
    fecha_fin = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.Nombre



class Proveedor(models.Model):
    ruc = models.CharField(unique=True,max_length=11)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=15,null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    certificado_eco = models.ForeignKey(CertificadoEco,  on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.razon_social