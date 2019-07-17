# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Cliente(models.Model):
    razon_social = models.CharField(max_length=150)
    cif = models.CharField( max_length=15)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=15,null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    #moroso = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)


    def __str__(self):
        return self.razon_social
