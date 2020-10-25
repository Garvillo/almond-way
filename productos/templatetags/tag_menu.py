from django import template
from django.shortcuts import render
from titulares.models import Titular
from productos.models import Impuestos



register = template.Library()

@register.simple_tag()
def get_titulares():
    titulares = Titular.objects.filter(disponible_para ="COMPRAS")
    return titulares

@register.simple_tag()
def get_impuestos():
    impuestos = Impuestos.objects.all()
    return impuestos