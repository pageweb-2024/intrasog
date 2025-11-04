import pandas as pd


datos = pd.read_csv("tablasIntraPueba.csv")
print(datos)

cantidad_original_datos = len(datos)
print("Cantidad original de datos:", cantidad_original_datos)

cantidad_posterior = len(datos)
print("Cantidad después del procesamiento:", cantidad_posterior)

dimension_de_impacto = cantidad_original_datos - cantidad_posterior
print("Se eliminaron", dimension_de_impacto, "registros por falta de ID_Paciente")