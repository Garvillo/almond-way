from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['cif', 'razon_social', 'direccion', 'telefono','correo', 'estado']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'estado':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

'''
class Cliente(models.Model):
    cif = models.CharField(unique=True,max_length=11)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15,null=True)
    correo = models.EmailField(null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.razon_social


class ListadoClientes(ListView):
    model = Cliente
    template_name = 'clientes.html'
    context_object_name = 'clientes'

class CrearCliente(CreateView):
    model = Cliente
    template_name = 'cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:listado_clientes')

class ModificarCliente(UpdateView):
    model = Cliente
    template_name = 'cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:listado_clientes')

class DetalleCliente(DetailView):
    model = Cliente
    template_name = 'detalle_cliente.html

'''