# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from proveedores.models import EntidadCertificadora, Proveedor


admin.site.register(Proveedor)
admin.site.register(EntidadCertificadora)



