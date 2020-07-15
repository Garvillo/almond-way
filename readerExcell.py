import pandas
import requests
import json

excel_data_df = pandas.read_excel('/home/garvi/Descargas/clientes.xlsx',
                                  sheet_name='cliente',
                                  usecols=['CODIGO',
                                           'NOMBRE',
                                           'DIRECCION',
                                           'CIUDAD',
                                           'CIF',
                                           'TELEFONO',
                                           'MOVIL',
                                           'FAX',
                                           'CORREOE',
                                           'URL',
                                           'CONTACTO',
                                           'FORMAPAGO',
                                           'DIASPAGO',
                                           'DOMICILIA',
                                           'LIBRE1'])
# print(excel_data_df)
for index, row in excel_data_df.iterrows():
    data = {
            "codigo": "" + str(row['CODIGO']) + "",
            "razon_social": "" + str(row['NOMBRE']) + "",
            "direccion": "" + str(row['DIRECCION']) + "",
            "ciudad": "" + str(row['CIUDAD']) + "",
            "ruc": "" + str(row['CIF']) + "",
            "telefono": "" + str(row['TELEFONO']) + "",
            "movil": "" + str(row['MOVIL']) + "",
            "fax": "" + str(row['FAX']) + "",
            "correoe": "" + str(row['CORREOE']) + "",
            "url": "" + str(row['URL']) + "",
            "contacto": "" + str(row['CONTACTO']) + "",
            "formapago": "" + str(row['FORMAPAGO']) + "",
            "diaspago": "" + str(row['DIASPAGO']) + "",
            "domicilia": "" + str(row['DOMICILIA']) + "",
            "observaciones": "" + str(row['LIBRE1']) + ""
    }
    jsonData = json.dumps(data)
    #print(jsonData)
    response = requests.post("http://127.0.0.1:8000/api/v1/new_proveedor", jsonData)
    print("Rspuesta: ", response.status_code)