from django.contrib import admin
from pagares.models import PagareCompra, PagareVenta


# Register your models here.
admin.site.register(PagareCompra)
admin.site.register(PagareVenta)