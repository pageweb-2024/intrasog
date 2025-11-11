import requests
from bs4 import BeautifulSoup
import re
from flask import Flask,jsonify,request

url2 = "https://www.intrasog.gov.co/notificaciones-cobro-coactivo/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
}

app = Flask(__name__)

registros2 = []
registrosJson = []
try:
    response2 = requests.get(url2, headers=headers)
    response2.raise_for_status()
    soup2 = BeautifulSoup(response2.text, 'html.parser')

    registros2 = soup2.find_all('td') 


    print("=== todas las infracciones ===\n")
    for i, td in enumerate(registros2, start=1):
        registrosJson.append(td.get_text(strip=True))
        texto = td.get_text(strip=True)
        print(f"{i}. Texto: {texto}")

    
except requests.exceptions.RequestException as e:
    print(f"Error al acceder a la página: {e}")

@app.route('/infraccion',methods=['GET'])
def listaTrabajadores():
    return registrosJson

if __name__ == '__main__':
    app.run(debug=True)