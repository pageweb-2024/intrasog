import pandas as pd
import mysql.connector

# Conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Aga-2014",
    database="intra2"
)

consulta_usuario = "SELECT * FROM usuario"
usuario = pd.read_sql(consulta_usuario, conexion)
print("Tabla Usuario:")
print(usuario)

consulta_comparendo = "SELECT * FROM comparendo"
comparendo = pd.read_sql(consulta_comparendo, conexion)
print("\nTabla Comparendo:")
print(comparendo)

consulta_infraccion = "SELECT * FROM infraccion"
infraccion = pd.read_sql(consulta_infraccion, conexion)
print("\nTabla Infraccion:")
print(infraccion)

conexion.close()
