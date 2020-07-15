# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class EntidadCertificadora(models.Model):
    nombre=  models.CharField(max_length=150, verbose_name=" Organismo de Certificación y Control")
    Observaciones =models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre



class Proveedor(models.Model):

    codigo = models.CharField(max_length=200, null=True, blank=True)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    ciudad = models.CharField(max_length=200, null=True, blank=True)
    ruc = models.CharField(max_length=11,verbose_name ="DNI/CIF")
    telefono = models.CharField(max_length=15,null=True, blank=True)
    movil = models.CharField(max_length=15,null=True, blank=True)
    fax = models.CharField(max_length=15,null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    url = models.CharField(max_length=150,null=True, blank=True)
    contacto = models.CharField(max_length=150,null=True, blank=True)
    formapago = models.CharField(max_length=150,null=True, blank=True)
    diaspago = models.CharField(max_length=150,null=True, blank=True)
    domicilia = models.CharField(max_length=150,null=True, blank=True)
    observaciones = models.CharField(max_length=150,null=True, blank=True)

    estado = models.BooleanField(default=True)

    entidad_certificadora = models.ForeignKey(EntidadCertificadora,  on_delete=models.CASCADE, blank=True, null=True)
    observaciones_eco = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.razon_social