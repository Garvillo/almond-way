from django.conf.urls import url



from .views import ListadoProductos, CrearProducto, ModificarProducto, DetalleProducto
from .views import CrearCompra, ModificarCompra, ListadoCompras

app_name = 'productos'

urlpatterns = [
    url(r'^silos', ListadoProductos.as_view(), name="listado_productos"),
    url(r'^crear_producto/$', CrearProducto.as_view(), name="crear_producto"),
    url(r'^modificar_producto/(?P<pk>.+)/$',ModificarProducto.as_view(), name="modificar_producto"),
    url(r'^detalle_producto/(?P<pk>.+)/$',DetalleProducto.as_view(), name="detalle_producto"),
    url(r'^crear_compra/$', CrearCompra.as_view(), name="crear_compra"),
    url(r'^modificar_compra/(?P<pk>.+)/$',ModificarCompra.as_view(), name="modificar_compra"),
    url(r'^compras/$', ListadoCompras.as_view(), name="listado_compras"),


   # url(r'^imprimir/(?P<pk>.+)/$', Html_to_pdf_view.as_view(), name="imprimir"),


]



