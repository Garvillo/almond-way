# -*- coding: utf-8 -*--
from __future__ import unicode_literals
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from .forms import ProductoForm,  CompraForm, DetalleCompraFormSet
from .forms import VentaForm, DetalleVentaFormSet
from .models import Producto,  Compra, DetalleCompra
from .models import Venta, DetalleVenta
from .models import Historico
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import django.utils.timezone

from django.core.mail import EmailMessage
from django.utils.safestring import mark_safe
from django.conf import settings
from .pdf import PdfRenderer
from django.core.mail import EmailMessage

from django.template.loader import render_to_string, get_template
import os
import xhtml2pdf.pisa as pisa
import base64
from django.contrib.staticfiles import finders

class ListadoComprasFiltradas(ListView):
    model = Compra
    template_name = 'compras.html'
    context_object_name = 'compras'

    def get_queryset(self):
        #mostramos las facturas de este año en orden descendente
        current_year = django.utils.timezone.now().year
        print(self)
        print(self.kwargs['imp'])
        return Compra.objects.filter(fecha__year = current_year,
                                     titular = self.kwargs['tit'],
                                     impuestos = self.kwargs['imp']).order_by('id')


class ListadoProductos(ListView):

    model = Producto
    template_name = 'productos_listado.html'
    context_object_name = 'productos'

#transacciones en un silo
class DetalleTransacciones(DetailView):
    model = Producto

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        '''
        Historico.objects.all().delete()

        self.object = self.get_object()
        detalles_compra = DetalleCompra.objects.filter(producto=self.object).order_by('pk')
        detalles_compra_dic = []
        kilos=0

        for detalle in detalles_compra:

            kilos += detalle.cantidad
            d = {#'producto': detalle.producto,
                 'cantidad': detalle.cantidad,
                 'precio_compra': detalle.precio_compra,
                 'id': detalle.compra.pk,
                 'fecha': detalle.fecha,
                 'proveedor': detalle.compra.proveedor,
                 'kilos_acumulados': kilos
            }
            detalles_compra_dic.append(d)
            Historico.objects.create(compra = detalle.compra,
                                     producto = detalle.producto,
                                     cantidad = detalle.cantidad,
                                     precio_compra = detalle.precio_compra,
                                     fecha = detalle.fecha,
                                     lote_heredado = detalle.lote_heredado,
                                     kilos_actuales = kilos)

        detalles_venta = DetalleVenta.objects.filter(producto=self.object).order_by('pk')
        detalles_venta_dic = []
       # kilos=0
        for detalle in detalles_venta:

            kilos -= detalle.cantidad
            d = {#'producto': detalle.producto,
                 'lote_heredado': detalle.lote_heredado,
                 'cantidad': detalle.cantidad,
                 'precio_venta': detalle.precio_venta,
                 'id': detalle.venta.pk,
                 'fecha': detalle.fecha,
                 'cliente': detalle.venta.cliente,
                 'kilos_acumulados': kilos
            }
            detalles_venta_dic.append(d)
            Historico.objects.create(venta = detalle.venta,
                                     producto = detalle.producto,
                                     cantidad = detalle.cantidad,
                                     precio_venta = detalle.precio_venta,
                                     fecha = detalle.fecha,
                                     lote_heredado = detalle.lote_heredado,
                                     kilos_actuales = kilos)


        #qkilos = Producto.objects.get(self.object)
        transacciones = Historico.objects.filter(producto=self.object).order_by('-fecha')
        
        return render(request, 'detalle_transacciones.html', {'compras': detalles_compra_dic,
                                                              'ventas': detalles_venta_dic,
                                                              'kilos': kilos})
        '''
        transacciones = Historico.objects.filter(producto=self.object).order_by('fecha')

        return render(request, 'detalle_transacciones_historico.html', {'transacciones': transacciones,
                                                                        'kilos': self.object.kilos})




class ListadoCompras(ListView):
    model = Compra
    template_name = 'compras.html'
    context_object_name = 'compras'

    def get_queryset(self):
        #mostramos las facturas de este año en orden descendente
        current_year = django.utils.timezone.now().year
        return Compra.objects.filter(fecha__year = current_year).order_by('id')

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
            #p = Producto.objects.get(descripcion=detalle.producto)
            #p.kilos = p.kilos + detalle.cantidad
            #p.save()

            detalle.producto.kilos += detalle.cantidad
            detalle.producto.save()

            # si el producto entra a un silo con lote
            if detalle.producto.lote:
                detalle.lote_heredado = detalle.producto.lote
                print("detalle lote", detalle.lote_heredado)
                detalle.save()
                #detalle.save(update_fields=["lote_heredado"])
                #DetalleVenta.objects.get(pk=detalle.pk).save(update_fields=["lote_heredado"])

            #qs = DetalleVenta.objects.get(pk =detalle.pk)
            #print("guardado en historico ", qs.producto, qs.cantidad, qs.precio_venta, qs.lote_heredado)
            Historico.objects.create(compra = detalle.compra,
                                     producto = detalle.producto,
                                     cantidad = detalle.cantidad,
                                     precio_compra = detalle.precio_compra,
                                     fecha = detalle.fecha,
                                     lote_heredado = detalle.lote_heredado,
                                     kilos_actuales= detalle.producto.kilos)


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

        ############# PDF ###################

        # obtenemos los detalles de esta facuta para crear un nested dict
        detalles = DetalleCompra.objects.filter(compra = form.instance.pk)
        lineas = {}
        i=1
        for d in detalles:
            detalle_total = d.precio_compra * d.cantidad
            lineas['linea'+str(i)] = {
                'producto': d.producto.variedad,
                'cantidad': d.cantidad,
                'precio': d.precio_compra,
                'total': detalle_total,
                'lote_heredado': d.lote_heredado
                         }
            i= i+1

        compra = Compra.objects.get(pk=form.instance.pk)
        context = {
            'numero': compra.nfact,
            'fecha': compra.fecha,
            'forma_pago': compra.forma_pago,
            'titular_nombre': compra.titular.nombre,
            'titular_cif': compra.titular.cif,
            'titular_direccion': compra.titular.direccion,
            'proveedor_nombre': compra.proveedor.razon_social,
            'proveedor_ruc': compra.proveedor.ruc,
            'proveedor_direccion': compra.proveedor.direccion,
            'proveedor_certificado': compra.proveedor.entidad_certificadora,
            'base': compra.base,
            'impuestos':compra.impuestos,
            'imp_aplicado': compra.imp_aplicado,
            'total': compra.total,
            'lineas': lineas
        }
        print(context)

        '''context = {
            'acta': qsacta,
            'laboratorio': qslaboratorio,
            'muestreo': qsmuestreo,
            'pk': pk,
            'tipo': tipo
        }'''


        template_path = 'plantilla_email.html'
        template = get_template(template_path)
        # html = template.render(form.instance.__dict__)
        html = template.render(context)
        # print(form.instance.__dict__)

        ## definir los datos del diccionario, este no sirve
        ## hacer bien los estilos, los de boostrap no funcionan
        ## los estilos que soporta estan bastante limitados
        ## https://xhtml2pdf.readthedocs.io/en/latest/reference.html#supported-css-properties

        ndocumento1 = "factura" + str(form.instance.nfact) + ".pdf"
        #ddocumento = os.path.join(settings.MEDIA_ROOT, ndocumento1)
        ddocumento = ndocumento1
        outFilename = ddocumento
        outFile = open(outFilename.encode("utf-8"), "w+b")
        pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=outFile, encoding='utf-8')
        outFile.close()
        ndocumento = ddocumento
        # ddocumento = os.path.join(settings.MEDIA_ROOT, ndocumento)
        leerdocumento = open(ddocumento.encode("utf-8"), "rb").read()

        ############### EMAIL ##################33

        b = base64.b64encode(leerdocumento).decode("utf-8", "ignore")

        nombredocumento = "factura" + str(form.instance.nfact) + ".pdf"
        email = "aurelio@syscomed.es"
        asunto = "Factura de compra"
        cuerpo = "Buenos dias, adjuntamos factura de compra"
        body = cuerpo
        # Replace this texto in plantilla cuerpo
        body_content = mark_safe(body)
        html_content = mark_safe(body_content)
        remitente = settings.EMAIL_HOST_USER
        destinatario = email
        try:
            msg = EmailMessage(asunto, html_content, remitente, [destinatario])
            msg.attach(nombredocumento, leerdocumento, "application/pdf")
            msg.content_subtype = "pdf"  # Main content is now text/html
            msg.encoding = 'utf-8'
            msg.send()
            print("mensaje enviado ")
        except Exception as e:
            print("no se ha podido enviar ", e)

        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_compra_form_set):
        return self.render_to_response(self.get_context_data(form=form, detalle_compra_form_set = detalle_compra_form_set))


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """

    result = finders.find(uri)

    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri
    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path



# Vista detalle de factura de compra
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



class DetailCompraPdf(DetailView):
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

        # return render(request, 'detail_compra.html', {'detalles': detalles_data, 'compra': compra})
        contexto= detalles_data + compra
        print("contexto", contexto)
        return contexto
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

            # Restamos los kilos de cada detalle en su almacen (silo)
            detalle.producto.kilos -= detalle.cantidad
            detalle.producto.save()

            # si el producto sale de un silo con lote
            if detalle.producto.lote:
                detalle.lote_heredado = detalle.producto.lote
                print("detalle lote", detalle.lote_heredado)
                detalle.save()
                #detalle.save(update_fields=["lote_heredado"])
                #DetalleVenta.objects.get(pk=detalle.pk).save(update_fields=["lote_heredado"])

            Historico.objects.create(venta = detalle.venta,
                                         producto = detalle.producto,
                                         cantidad = detalle.cantidad,
                                         precio_venta = detalle.precio_venta,
                                         fecha = detalle.fecha,
                                         lote_heredado = detalle.lote_heredado,
                                         kilos_actuales= detalle.producto.kilos)

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
                 'lote_heredado': detalle.lote_heredado,
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


