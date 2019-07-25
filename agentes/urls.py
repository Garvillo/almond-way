from django.conf.urls import url
from .views import ListadoAgentes, CrearAgente, ModificarAgente, DetalleAgente

app_name = 'agentes'

urlpatterns = [
    url(r'^listado/$', ListadoAgentes.as_view(), name="listado_agentes"),
    url(r'^crear_agente/$', CrearAgente.as_view(), name="crear_agente"),
    url(r'^modificar_agente/(?P<pk>.+)/$',ModificarAgente.as_view(), name="modificar_agente"),
    url(r'^detalle_agente/(?P<pk>.+)/$',DetalleAgente.as_view(), name="detalle_agente"),

]