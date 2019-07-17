# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from .forms import ProveedorForm
from .models import Proveedor
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.http.response import HttpResponseRedirect



class DetalleProveedor(DetailView):
    model = Proveedor
    template_name = 'detalle_proveedor.html'


class CrearProveedor(CreateView):
    template_name = 'proveedor_nuevo.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('productos:listado_proveedores')


class ListadoProveedores(ListView):
    model = Proveedor
    template_name = 'proveedores_listado.html'
    context_object_name = 'proveedores'

class ModificarProveedor(UpdateView):
    model = Proveedor
    template_name = 'proveedor_modificar.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('productos:listado_proveedores')
