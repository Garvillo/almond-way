"""modales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [


    url(r'^login/', LoginView.as_view(template_name='login.html'), name="login"),
    url(r'^logout/', LogoutView.as_view(template_name='login.html'), name="logout"),
    url(r'^admin/', admin.site.urls),
    url(r'^productos/', include('productos.urls', namespace='productos')),
    url(r'^cliente/', include('clientes.urls', namespace='clientes')),
    url(r'^proveedor/', include('proveedores.urls', namespace='proveedores')),
    url(r'^home', views.home, name='home'),
    url(r'^', views.home, name='home'),
]



