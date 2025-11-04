from flask import Flask, jsonify
from flask_cors import CORS
import pymysql

from clases import usuario
from clases import infraccion
from clases import comparendo

app = Flask(__name__)
CORS(app)

db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Aga-2014",
    database="intra2"
)

@app.route('/usuario', methods=['GET'])
def obtener_usuario():
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM usuario")
    filas = cursor.fetchall()
    cursor.close()
    lista_usuarios = []
    for fila in filas:
        u = usuario(
            fila['idUsuario'],
            fila['nombre'],
            fila['apellido'],
            fila['correo'],
            fila['telefono'],
            fila['fechaRegistro']
        )
        lista_usuarios.append(u.to_json()) 
    return jsonify(lista_usuarios)
    
@app.route('/infraccion', methods=['GET'])
def obtener_infracciones():
    cursor2 = db.cursor(pymysql.cursors.DictCursor)
    cursor2.execute("SELECT * FROM infraccion")
    filas2 = cursor2.fetchall()
    cursor2.close()
    lista_infraccion = []
    for fila2 in filas2:
        i = infraccion(
            fila2['idInfraccion'],
            fila2['tipoInfraccion'],
            fila2['descripcion'],
            fila2['multa'],
        )
        lista_infraccion.append(i.to_json()) 
    return jsonify(lista_infraccion)

@app.route('/comparendo', methods=['GET'])
def obtener_comparendos():
    cursor3 = db.cursor(pymysql.cursors.DictCursor)
    cursor3.execute("SELECT * FROM comparendo")
    filas3 = cursor3.fetchall()
    cursor3.close()
    lista_comparendo = []
    for fila3 in filas3:
        c = comparendo(
            fila3['numComparendo'],
            fila3['idUsuario'],
            fila3['idInfraccion'],
            str(fila3['fecha']),
            str(fila3['hora']),
            fila3['lugar']
        )
        lista_comparendo.append(c.to_json()) 
    return jsonify(lista_comparendo)


if __name__ == '__main__':
    app.run(debug=True)