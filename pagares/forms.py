from django import forms
from .models import PagareCompra, PagareVenta
import django.utils.timezone
from django.forms import DateField
from django.conf import settings

class PagareCompraForm(forms.ModelForm):

    class Meta:

        model = PagareCompra
        fields = ['compra',
                  'numero',
                  'fecha_emitido',
                  'fecha_cobrado',
                  'fecha_vencimiento',
                  'cobrado',
                  'observaciones']

    def __init__(self, *args, **kwargs):
        super(PagareCompraForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                    'class': 'form-control'
            })

class PagareVentaForm(forms.ModelForm):

    class Meta:
        model = PagareVenta
        fields = ['venta',
                  'numero',
                  'fecha_emitido',
                  'fecha_cobrado',
                  'fecha_vencimiento',
                  'cobrado',
                  'observaciones']

    def __init__(self, *args, **kwargs):
        super(PagareVentaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
