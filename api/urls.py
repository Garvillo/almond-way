from django.conf.urls import url

from .views import AddProveedor
urlpatterns = [
    url('^new_proveedor', AddProveedor.as_view(), name="new_proveedor"),
]
