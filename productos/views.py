# -*- coding: utf-8 -*--
from __future__ import unicode_literals
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from .forms import ProductoForm,  CompraForm, DetalleCompraFormSet
from .forms import VentaForm, DetalleVentaFormSet
from .models import Producto,  Compra, DetalleCompra
from .models import Venta, DetalleVenta

from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class ListadoProductos(ListView):

    model = Producto
    template_name = 'productos_listado.html'
    context_object_name = 'productos'

#transacciones en un silo
class DetalleTransacciones(DetailView):
    model = Producto

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object.kilos)
        #form_class = self.get_form_class()
        #form = self.get_form(form_class)
        #todos los detalles de compra para este producto/silo

        detalles_compra = DetalleCompra.objects.filter(producto=self.object).order_by('pk')
        detalles_compra_dic = []
        kilos=0
        for detalle in detalles_compra:

            kilos += detalle.cantidad
            d = {'producto': detalle.producto,
                 'cantidad': detalle.cantidad,
                 'precio_compra': detalle.precio_compra,
                 'id': detalle.compra.pk,
                 'fecha': detalle.fecha,
                 'proveedor': detalle.compra.proveedor,
                 'kilos_acumulados': kilos
            }
            detalles_compra_dic.append(d)

        detalles_venta = DetalleVenta.objects.filter(producto=self.object).order_by('pk')
        detalles_venta_dic = []
       # kilos=0
        for detalle in detalles_venta:

            kilos -= detalle.cantidad
            d = {'producto': detalle.producto,
                 'cantidad': detalle.cantidad,
                 'precio_venta': detalle.precio_venta,
                 'id': detalle.venta.pk,
                 'fecha': detalle.fecha,
                 'cliente': detalle.venta.cliente,
                 'kilos_acumulados': kilos
            }
            detalles_venta_dic.append(d)

        #return self.render_to_response(self.get_context_data(form=form, detalle_compra_form_set=detalle_compra_form_set))

        return render(request, 'detalle_transacciones.html', {'compras': detalles_compra_dic,
                                                              'ventas': detalles_venta_dic,
                                                              'kilos': kilos})




class ListadoCompras(ListView):
    model = Compra
    template_name = 'compras.html'
    context_object_name = 'compras'

class ListadoVentas(ListView):
    model = Venta
    template_name = 'ventas.html'
    context_object_name = 'ventas'


class CrearProducto(CreateView):
    template_name = 'producto_nuevo.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listado_productos')

class ModificarProducto(UpdateView):
    model = Producto
    template_name = 'producto_modificar.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listado_productos')


class ModificarCompra(UpdateView):
    model = Compra
    template_name = 'compra.html'
    form_class = CompraForm
    success_url = reverse_lazy('productos:listado_compras')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalles = DetalleCompra.objects.filter(compra=self.object).order_by('pk')
        detalles_data = []
        for detalle in detalles:
            d = {'producto': detalle.producto,
                 'cantidad': detalle.cantidad,
                 'precio_compra': detalle.precio_compra}
            detalles_data.append(d)
        detalle_compra_form_set = DetalleCompraFormSet(initial=detalles_data)
        return self.render_to_response(self.get_context_data(form=form, detalle_compra_form_set=detalle_compra_form_set))


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_compra_form_set = DetalleCompraFormSet(request.POST)
        if form.is_valid() and detalle_compra_form_set.is_valid():
            return self.form_valid(form, detalle_compra_form_set)
        else:
            return self.form_invalid(form, detalle_compra_form_set)


    def form_valid(self, form, detalle_compra_form_set):
        self.object = form.save()
        detalle_compra_form_set.instance = self.object
        DetalleCompra.objects.filter(compra = self.object).delete()
        detalle_compra_form_set.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_compra_form_set):
        return self.render_to_response(self.get_context_data(form=form, detalle_compra_form_set = detalle_compra_form_set))




class CrearCompra(CreateView):
    model = Compra
    template_name = 'compra.html'
    form_class = CompraForm
    success_url = reverse_lazy('productos:listado_compras')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_orden_compra_formset=DetalleCompraFormSet()
        return self.render_to_response(self.get_context_data(form=form, detalle_compra_form_set=detalle_orden_compra_formset))

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_compra_form_set = DetalleCompraFormSet(request.POST)
        if form.is_valid() and detalle_compra_form_set.is_valid():
            return self.form_valid(form, detalle_compra_form_set)
        else:
            return self.form_invalid(form, detalle_compra_form_set)


    def form_valid(self, form, detalle_compra_form_set):

        #obtenemos la ultima de su  serie prara generar un nuevo numero
        qsComp_last=Compra.objects.filter(lfact=form.instance.titular.letra).order_by('nfact').last()

        if qsComp_last:
            form.instance.nfact = qsComp_last.nfact+1
        else:
            form.instance.nfact = 1
        form.instance.lfact = form.instance.titular.letra





        self.object = form.save()
        detalle_compra_form_set.instance = self.object
        detalle_compra_form_set.save()
        total_base =  0

        detalles = DetalleCompra.objects.filter(compra=self.object).order_by('pk')
        for detalle in detalles:
            d = {'producto': detalle.producto,
                 'cantidad': detalle.cantidad,
                 'precio_compra': detalle.precio_compra}

            #sumamos los kilos de cada detalle en su almacen(silo)
            p = Producto.objects.get(descripcion=detalle.producto)
            p.kilos = p.kilos + detalle.cantidad
            p.save()

            #calculamos su precio base
            total_detalle = detalle.cantidad * detalle.precio_compra
            print("valores en €")
            print (detalle.producto, total_detalle)
            total_base = total_base + total_detalle



        print("base ", total_base )
        #aplicamos impuestos
        form.instance.base = total_base
        form.instance.imp_aplicado =  total_base * form.instance.impuestos.impuesto1/100
        print("valor de impuestto 1 ", form.instance.imp_aplicado )
        #Comprobamos si hay un segundo impuesto a aplicar
        if form.instance.impuestos.impuesto2:
            if form.instance.impuestos.se_calcula_con == "BASE":
                form.instance.imp_aplicado = form.instance.imp_aplicado + total_base * form.instance.impuestos.impuesto2/100
                print("calculando impuesto 2 BASE ", form.instance.imp_aplicado)
            if form.instance.impuestos.se_calcula_con == "TOTAL":
                form.instance.imp_aplicado = form.instance.imp_aplicado + (form.instance.imp_aplicado+total_base)  * form.instance.impuestos.impuesto2/100
                print("calculando impuesto 2 TOTAL", form.instance.imp_aplicado)
        form.instance.total = total_base + form.instance.imp_aplicado

        print("impuestos ",form.instance.imp_aplicado)
        print("total", form.instance.total)

        form.instance.save()

        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_compra_form_set):
        return self.render_to_response(self.get_context_data(form=form, detalle_compra_form_set = detalle_compra_form_set))



# factura de compra
class DetailCompra(DetailView):
    model = Compra
    #template_name = 'detalle_producto.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("-"*10)
        print(self.object.base)
        print(self.object.numero)
        #form_class = self.get_form_class()
        #form = self.get_form(form_class)
        #todos los detalles de compra para este producto/silo
        compra = self.object

        detalles = DetalleCompra.objects.filter(compra=self.object).order_by('pk')
        detalles_data = []
        kilos=0
        for detalle in detalles:

            kilos += detalle.cantidad
            d = {'producto': detalle.producto,
                 'cantidad': detalle.cantidad,
                 'precio_compra': detalle.precio_compra,
                 'total_detalle': (detalle.precio_compra * detalle.cantidad)

                 #'id': detalle.compra.pk,
                 #'fecha': detalle.fecha,
                 #'proveedor': detalle.compra.proveedor,
                 #'kilos_acumulados': kilos
                 }
            detalles_data.append(d)


        #return self.render_to_response(self.get_context_data(form=form, detalle_compra_form_set=detalle_compra_form_set))

        return render(request, 'detail_compra.html', {'detalles': detalles_data, 'compra': compra})

# -----------------------------  ventas  ---------------------------------


class CrearVenta(CreateView):
    model = Venta
    template_name = 'venta.html'
    form_class = VentaForm
    success_url = reverse_lazy('productos:listado_ventas')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_orden_venta_formset = DetalleVentaFormSet()
        return self.render_to_response(self.get_context_data(form=form, detalle_venta_form_set = detalle_orden_venta_formset))

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_venta_form_set = DetalleVentaFormSet(request.POST)
        if form.is_valid() and detalle_venta_form_set.is_valid():
            return self.form_valid(form, detalle_venta_form_set)
        else:
            return self.form_invalid(form, detalle_venta_form_set)


    def form_valid(self, form, detalle_venta_form_set):

        #obtenemos la ultima de su  serie prara generar un nuevo numero
        qsComp_last = Venta.objects.filter(lfact=form.instance.titular.letra).order_by('nfact').last()

        if qsComp_last:
            form.instance.nfact = qsComp_last.nfact+1
        else:
            form.instance.nfact = 1
        form.instance.lfact = form.instance.titular.letra

        self.object = form.save()
        detalle_venta_form_set.instance = self.object
        detalle_venta_form_set.save()
        total_base =  0

        detalles = DetalleVenta.objects.filter(venta=self.object).order_by('pk')
        for detalle in detalles:
            d = {'producto': detalle.producto,
                 'cantidad': detalle.cantidad,
                 'precio_venta': detalle.precio_venta}

            #sumamos los kilos de cada detalle en su almacen(silo)
            p = Producto.objects.get(descripcion = detalle.producto)
            p.kilos -=  detalle.cantidad
            p.save()

            #calculamos su precio base
            total_detalle = detalle.cantidad * detalle.precio_venta
            print("valores en €")
            print (detalle.producto, total_detalle)
            total_base = total_base + total_detalle

        print("base ", total_base )
        #aplicamos impuestos
        form.instance.base = total_base
        form.instance.imp_aplicado =  total_base * form.instance.impuestos.impuesto1/100
        print("valor de impuestto 1 ", form.instance.imp_aplicado )
        #Comprobamos si hay un segundo impuesto a aplicar
        if form.instance.impuestos.impuesto2:
            if form.instance.impuestos.se_calcula_con == "BASE":
                form.instance.imp_aplicado = form.instance.imp_aplicado + total_base * form.instance.impuestos.impuesto2/100
                print("calculando impuesto 2 BASE ", form.instance.imp_aplicado)
            if form.instance.impuestos.se_calcula_con == "TOTAL":
                form.instance.imp_aplicado = form.instance.imp_aplicado + (form.instance.imp_aplicado+total_base)  * form.instance.impuestos.impuesto2/100
                print("calculando impuesto 2 TOTAL", form.instance.imp_aplicado)
        form.instance.total = total_base + form.instance.imp_aplicado

        print("impuestos ",form.instance.imp_aplicado)
        print("total", form.instance.total)

        form.instance.save()

        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_venta_form_set):
        return self.render_to_response(self.get_context_data(form=form, detalle_venta_form_set = detalle_venta_form_set))



# factura de venta
class DetailVenta(DetailView):
    model = Venta
    #template_name = 'detalle_producto.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("-"*10)
        print(self.object.base)
        print(self.object.numero)
        #form_class = self.get_form_class()
        #form = self.get_form(form_class)
        #todos los detalles de compra para este producto/silo
        venta = self.object

        detalles = DetalleVenta.objects.filter(venta=self.object).order_by('pk')
        detalles_data = []
        kilos=0
        for detalle in detalles:

            kilos += detalle.cantidad
            d = {'producto': detalle.producto,
                 'cantidad': detalle.cantidad,
                 'precio_venta': detalle.precio_venta,
                 'total_detalle': (detalle.precio_venta * detalle.cantidad)

                 #'id': detalle.compra.pk,
                 #'fecha': detalle.fecha,
                 #'proveedor': detalle.compra.proveedor,
                 #'kilos_acumulados': kilos
                 }
            detalles_data.append(d)


        #return self.render_to_response(self.get_context_data(form=form, detalle_compra_form_set=detalle_compra_form_set))

        return render(request, 'detail_venta.html', {'detalles': detalles_data, 'venta': venta })


