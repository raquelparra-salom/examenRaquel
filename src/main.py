from flask import Flask
from flask import request, redirect, url_for
from flask import make_response
from flask import render_template
import os

app =  Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    return render_template("index.html")

@app.route('/gastos', methods=['POST'])
def pagos():

    gasolina = request.form['gasolina']
    seguro = request.form['seguro']
    itv = request.form['itv']
    aceite = request.form['aceite']

    gastos = int(gasolina) + int(seguro) + int(itv) + int(aceite)

    diccionario = {
        "enero": gastos,
        "febrero": gastos,
        "marzo": gastos,
        "abril": gastos,
        "mayo": gastos,
        "junio": gastos,
        "julio": gastos,
        "agosto": gastos,
        "septiembre": gastos,
        "octubre": gastos,
        "noviembre": gastos,
        "diciembre": gastos,
    }

    print(gastos)
    return render_template("play.html", diccionario=diccionario)

   

if __name__ == '__main__' :
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)