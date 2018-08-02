from django.conf.urls import url
from .views import ListadoClientes, CrearCliente, ModificarCliente, DetalleCliente

app_name = 'clientes'

urlpatterns = [
    url(r'^listado/$', ListadoClientes.as_view(), name="listado_clientes"),
    url(r'^crear_cliente/$', CrearCliente.as_view(), name="crear_cliente"),
    url(r'^modificar_cliente/(?P<pk>.+)/$',ModificarCliente.as_view(), name="modificar_cliente"),
    url(r'^detalle_cliente/(?P<pk>.+)/$',DetalleCliente.as_view(), name="detalle_cliente"),

]