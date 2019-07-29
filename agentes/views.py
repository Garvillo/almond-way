# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from .forms import AgenteForm
from .models import Agente
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.http.response import HttpResponseRedirect


class ListadoAgentes(ListView):
    model = Agente
    template_name = 'agentes_listado.html'
    context_object_name = 'agentes'

class CrearAgente(CreateView):
    model = Agente
    template_name = 'agente_nuevo.html'
    form_class = AgenteForm
    success_url = reverse_lazy('agentes:listado_agentes')

class ModificarAgente(UpdateView):
    model = Agente
    template_name = 'agente_modificar.html'
    form_class = AgenteForm
    success_url = reverse_lazy('agentes:listado_agentes')

class DetalleAgente(DetailView):
    model = Agente
    template_name = 'agente_detalle.html'