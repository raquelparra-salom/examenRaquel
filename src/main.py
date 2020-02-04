from flask import Flask
from flask import request, redirect, url_for
from flask import make_response
from flask import render_template
import os
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["examen"]
agenda = mydb["agenda"]
app =  Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/gastos', methods=['POST'])
def pagos():

    gasolina = request.form['gasolina']
    seguro = request.form['seguro']
    itv = request.form['itv']
    aceite = request.form['aceite']

    gastos = int(gasolina) + int(seguro) + int(itv) + int(aceite)

    diccionario = {
        "enero": int(gasolina), 
        "febrero": int(gasolina) + int(seguro), 
        "marzo": int(gasolina), 
        "abril": int(gasolina) + int(aceite), 
        "mayo": int(gasolina), 
        "junio": int(gasolina) + int(itv), 
        "julio": int(gasolina), 
        "agosto": int(gasolina), 
        "septiembre": int(gasolina), 
        "octubre": int(gasolina), 
        "noviembre": int(gasolina), 
        "diciembre": int(gasolina),
        }
    agenda.insert_one(diccionario)

    print(gastos)
    return render_template("resultado.html", gastos=gastos)

if __name__ == '__main__' :
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)