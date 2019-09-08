# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from .forms import PagareCompraForm, PagareVentaForm
from .models import PagareCompra, PagareVenta
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
import django.utils.timezone
from django.http.response import HttpResponseRedirect


class ListadoPagaresCompra(ListView):
    model = PagareCompra
    template_name = 'pagare_compra_listado.html'
    context_object_name = 'pagares'

class CrearPagareCompra(CreateView):
    model = PagareCompra
    template_name = 'pagare_compra_nuevo.html'
    form_class = PagareCompraForm
    success_url = reverse_lazy('pagares:listado_pagares_compra')


class ModificarPagareCompra(UpdateView):
    model = PagareCompra
    template_name = 'pagare_compra_modificar.html'
    form_class = PagareCompraForm
    success_url = reverse_lazy('pagares:listado_pagares_compra')

class DetallePagareCompra(DetailView):
    model = PagareCompra
    template_name = 'pagare_compra_detalle.html'



class ListadoPagaresVenta(ListView):
    model = PagareVenta
    template_name = 'pagare_venta_listado.html'
    context_object_name = 'pagares'

class CrearPagareVenta(CreateView):
    model = PagareVenta
    template_name = 'pagare_venta_nuevo.html'
    form_class = PagareVentaForm
    success_url = reverse_lazy('pagares:listado_pagares_venta')

    def form_valid(self, form):
        form.instance.fecha_emitido = django.utils.timezone.now()

        return super(CrearPagareVenta, self).form_valid(form)

class ModificarPagareVenta(UpdateView):
    model = PagareVenta
    template_name = 'pagare_venta_modificar.html'
    form_class = PagareVentaForm
    success_url = reverse_lazy('pagares:listado_pagares_venta')

class DetallePagareVenta(DetailView):
    model = PagareVenta
    template_name = 'pagare_venta_detalle.html'