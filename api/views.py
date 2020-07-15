import datetime
import json
import math

from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from proveedores.models import Proveedor

class JSONMixin(object):

    def default_response(self):
        return {
            "ts": "" + str(int(datetime.datetime.now().timestamp() * 1000)) + "",
            "status": "default response"
        }

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if not response:
            response = self.default_response()

        if type(response) == dict:
            return HttpResponse(json.dumps(response), content_type="application/json")

        return response


class AddProveedor(JSONMixin, View):
    def post(self, request, *args, **kwargs):
        body = request.body
        try:
            datos = json.loads(body.decode("utf-8"))
            #print (datos)
        except Exception as e:
            codjson = " Json mal formado, no se puede parsear: " + str(e)
            return JsonResponse({'status': 'Peticion no procesada', 'message': codjson}, status=400)
        try:
            codigo = datos['codigo']
            razon_social = datos['razon_social']
            direccion = datos['direccion']
            if direccion == "nan":
                direccion = ""
            ciudad = datos['ciudad']
            if ciudad == "nan":
                ciudad =""
            ruc = datos['ruc']
            if ruc == "nan":
                rux =""
            telefono = datos['telefono']
            if telefono == "nan":
                telefono=""
            movil = datos['movil']
            if movil== "nan":
                movil=""
            fax = datos['fax']
            if fax== "nan":
                fax=""
            correoe = datos['correoe']
            if correoe== "nan":
                correoe=""
            url = datos['url']
            if url== "nan":
                url=""
            contacto = datos['contacto']
            if contacto== "nan":
                contacto=""
            formapago = datos['formapago']
            if formapago== "nan":
                formapago=""
            diaspago = datos['diaspago']
            if diaspago== "nan":
                diaspago=""
            domicilia = datos['domicilia']
            if domicilia== "nan":
                domicilia=""
            observaciones = datos['observaciones']
            if observaciones== "nan":
                observaciones=""

            # Si el proveedor existe se actualiza
            if Proveedor.objects.filter(codigo=codigo):
                print("El proveedor existe")

            else:
                prov = Proveedor(codigo = codigo,
                            razon_social = razon_social,
                            direccion = direccion,
                            ciudad = ciudad,
                            ruc = ruc,
                            telefono = telefono,
                            movil = movil,
                            fax = fax,
                            correo = correoe,
                            url = url,
                            contacto = contacto,
                            formapago = formapago,
                            diaspago = diaspago,
                            domicilia = domicilia,
                            observaciones = observaciones)
                prov.save()
                print("Proveedor se ha creado")


        except Exception as e:
            print(e, "exception")
