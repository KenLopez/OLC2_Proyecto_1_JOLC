from types import resolve_bases
from flask import Flask, render_template, url_for, redirect, request
from classes.Global import Global
import analizador.gramatica as g

app = Flask(__name__)

@app.route("/Compile", methods=["POST", "GET"])
def compile():
    main = Global()
    entrada=''
    if request.method == "POST":
        entrada = request.form["entrada"]
        main.instrucciones = g.parse(entrada)
        main.execute()
    return render_template('index.html', result=main, text=entrada)

@app.route("/")
def index():
    return redirect("Compile")

if __name__ == '__main__':
    app.run(debug=True)
