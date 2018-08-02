# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Cliente(models.Model):
    cif = models.CharField(unique=True,max_length=11)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15,null=True)
    correo = models.EmailField(null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.razon_social
