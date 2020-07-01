import pandas

excel_data_df = pandas.read_excel('clientes.xlsx', sheet_name='cliente', usecols=['CODIGO',
                                                                                  'NOMBRE',
                                                                                  'DIRECCION',
                                                                                  'CIUDAD',
                                                                                  'CIF',
                                                                                  'MOVIL',
                                                                                  'FAX',
                                                                                  'TELEFONO'])
# print(excel_data_df)
for index, row in excel_data_df.iterrows():
    print(row['CODIGO'],"|",
          row['NOMBRE'],"|",
          row['CIF'],"|",
          row['DIRECCION'],"|",
          row['CIUDAD'],"|",
          row['TELEFONO'],"|",
          row['MOVIL'],"|",
          row['FAX'])

