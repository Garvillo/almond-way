from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['ruc',
                  'razon_social',
                  'direccion',
                  'telefono',
                  'correo',
                  'estado',
                  'entidad_certificadora',
                  'observaciones_eco']

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'estado':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })