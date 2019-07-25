from django import forms
from .models import Agente


class AgenteForm(forms.ModelForm):

    class Meta:
        model = Agente
        fields = ['cif',
                  'nombre',
                  'observaciones',
                  'direccion',
                  'telefono',
                  'correo',
                  'activo']

    def __init__(self, *args, **kwargs):
        super(AgenteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                    'class': 'form-control'
            })

'''
c    nombre = models.CharField(max_length=150)
    cif = models.CharField(unique=True, max_length=11, null=True, blank=True)
    observaciones = models.CharField(max_length=500, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=15,null=True, blank=True)
    correo = models.EmailField( null=True, blank=True)
    activo = models.BooleanField(default=True)



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