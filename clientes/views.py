# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from .forms import ClienteForm
from .models import Cliente
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.http.response import HttpResponseRedirect


class ListadoClientes(ListView):
    model = Cliente
    template_name = 'clientes_listado.html'
    context_object_name = 'clientes'

class CrearCliente(CreateView):
    model = Cliente
    template_name = 'cliente_nuevo.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:listado_clientes')

class ModificarCliente(UpdateView):
    model = Cliente
    template_name = 'cliente_modificar.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:listado_clientes')

class DetalleCliente(DetailView):
    model = Cliente
    template_name = 'detalle_cliente.html'