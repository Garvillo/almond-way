from django.conf.urls import url



from .views import ListadoProductos, CrearProducto, ModificarProducto, DetalleTransacciones
from .views import CrearCompra, ModificarCompra, ListadoCompras, DetailCompra
from .views import CrearVenta, ListadoVentas, DetailVenta

app_name = 'productos'

urlpatterns = [
    url(r'^silos', ListadoProductos.as_view(), name="listado_productos"),
    url(r'^crear_producto/$', CrearProducto.as_view(), name="crear_producto"),
    url(r'^modificar_producto/(?P<pk>.+)/$',ModificarProducto.as_view(), name="modificar_producto"),
    url(r'^detalle_transaciones/(?P<pk>.+)/$',DetalleTransacciones.as_view(), name="detalle_transacciones"),

    url(r'^crear_compra/$', CrearCompra.as_view(), name="crear_compra"),
    url(r'^modificar_compra/(?P<pk>.+)/$',ModificarCompra.as_view(), name="modificar_compra"),
    url(r'^detalle_compra/(?P<pk>.+)/$',DetailCompra.as_view(), name="detalle_compra"),
    url(r'^compras/$', ListadoCompras.as_view(), name="listado_compras"),

    url(r'^crear_venta/$', CrearVenta.as_view(), name="crear_venta"),
    #url(r'^modificar_compra/(?P<pk>.+)/$', ModificarCompra.as_view(), name="modificar_compra"),
    url(r'^detalle_venta/(?P<pk>.+)/$', DetailVenta.as_view(), name="detalle_venta"),
    url(r'^ventas/$', ListadoVentas.as_view(), name="listado_ventas"),

   # url(r'^imprimir/(?P<pk>.+)/$', Html_to_pdf_view.as_view(), name="imprimir"),


]



