from django.conf.urls import url
from .views import ListadoPagaresCompra, CrearPagareCompra, ModificarPagareCompra, DetallePagareCompra
from .views import ListadoPagaresVenta, CrearPagareVenta, ModificarPagareVenta, DetallePagareVenta

app_name = 'pagares'

urlpatterns = [
    url(r'^listado_pagare_compra/$', ListadoPagaresCompra.as_view(), name="listado_pagares_compra"),
    url(r'^listado_pagare_venta/$', ListadoPagaresVenta.as_view(), name="listado_pagares_venta"),
    url(r'^crear_pagare_compra/$', CrearPagareCompra.as_view(), name="crear_pagare_compra"),
    url(r'^crear_pagare_venta/$', CrearPagareVenta.as_view(), name="crear_pagare_venta"),
    url(r'^modificar_pagare_compra/(?P<pk>.+)/$',ModificarPagareCompra.as_view(), name="modificar_pagare_compra"),
    url(r'^modificar_pagare_venta/(?P<pk>.+)/$',ModificarPagareVenta.as_view(), name="modificar_pagare_venta"),
    url(r'^detalle_pagare_compra/(?P<pk>.+)/$',DetallePagareCompra.as_view(), name="detalle_pagare_compra"),
    url(r'^detalle_pagare_venta/(?P<pk>.+)/$',DetallePagareVenta.as_view(), name="detalle_pagare_venta"),

]
