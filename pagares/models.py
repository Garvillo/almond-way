from django.db import models
from productos.models import Compra, Venta
from django_extensions.db.models import TimeStampedModel
import django.utils.timezone


class PagareCompra(TimeStampedModel):

    compra =  models.ForeignKey(Compra, on_delete=models.CASCADE)
    numero =  models.CharField(max_length=25,null=True, blank=True)

    fecha_emitido = models.DateField(blank=True, null=True)
    fecha_cobrado = models.DateField( blank=True, null=True)
    fecha_vencimiento = models.DateField( blank=True, null=True)
    cobrado = models.BooleanField(default=False)
    observaciones = models.CharField(max_length=250, blank=True, null=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.numero



class PagareVenta(TimeStampedModel):

    venta =  models.ForeignKey(Venta, on_delete=models.CASCADE)
    fecha_emitido = models.DateField(editable=True)

    numero =  models.CharField(max_length=25,null=True, blank=True)
    fecha_cobrado = models.DateField( blank=True, null=True, editable=True)
    fecha_vencimiento = models.DateField( blank=True, null=True, editable=True)
    cobrado = models.BooleanField(default=False)
    observaciones = models.CharField(max_length=250, blank=True, null=True)


    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.numero