from django.conf.urls import url
from .views import ListadoProveedores, CrearProveedor, DetalleProveedor, ModificarProveedor

app_name = 'proveedores'

urlpatterns = [

    url(r'^listado/$', ListadoProveedores.as_view(), name="listado_proveedores"),
    url(r'^crear_proveedor/$', CrearProveedor.as_view(), name="crear_proveedor"),
    url(r'^detalle_proveedor/(?P<pk>.+)/$',DetalleProveedor.as_view(), name="detalle_proveedor"),
    url(r'^modificar_proveedor/(?P<pk>.+)/$',ModificarProveedor.as_view(), name="modificar_proveedor"),


]