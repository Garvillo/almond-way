from django import forms
from django.forms.models import modelformset_factory, inlineformset_factory
from .models import Producto, Proveedor, Compra, DetalleCompra
from .models import Cliente, Venta, DetalleVenta


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['descripcion', 'variedad', 'lote']

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            if field != 'estado':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


# COMPRAS -------------------------------------------------------
class CompraForm(forms.ModelForm):

    class Meta:
        model = Compra
        fields = ['titular', 'proveedor', 'agente', 'forma_pago', 'impuestos']

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):


            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })




class DetalleCompraForm(forms.ModelForm):

    class Meta:
        model = DetalleCompra
        fields = ['producto','cantidad','precio_compra']

    def __init__(self, *args, **kwargs):
        super(DetalleCompraForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad == '':
            raise forms.ValidationError("Debe ingresar una cantidad valida")
        return cantidad

    def clean_precio_compra(self):
        precio = self.cleaned_data['precio_compra']
        if precio == '':
            raise forms.ValidationError("Debe ingresar un precio valido")
        return precio

DetalleCompraFormSet = inlineformset_factory(Compra, DetalleCompra, form=DetalleCompraForm, extra=4 )

# VENTAS ------------------------------------------------------------

class VentaForm(forms.ModelForm):

    class Meta:
        model = Venta
        fields = ['titular', 'cliente', 'agente', 'forma_pago', 'impuestos']

    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):


            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class DetalleVentaForm(forms.ModelForm):

    class Meta:
        model = DetalleVenta
        fields = ['producto','cantidad','precio_venta']

    def __init__(self, *args, **kwargs):
        super(DetalleVentaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad == '':
            raise forms.ValidationError("Debe ingresar una cantidad valida")
        return cantidad

    def clean_precio_compra(self):
        precio = self.cleaned_data['precio_venta']
        if precio == '':
            raise forms.ValidationError("Debe ingresar un precio valido")
        return precio

DetalleVentaFormSet = inlineformset_factory(Venta, DetalleVenta, form=DetalleVentaForm, extra=4 )