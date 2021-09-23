from io import SEEK_CUR
from types import resolve_bases
from flask import Flask, render_template, url_for, redirect, request, session
from classes.Global import Global
import analizador.gramatica as g
import graphviz
import base64
import sys
sys.setrecursionlimit(4000)

app = Flask(__name__)
app.secret_key = "201906570"

@app.route("/Compile", methods=["POST", "GET"])
def compile():
    main = Global()
    entrada=''
    if 'entrada' in session:
        entrada = session["entrada"]
    if 'salida' in session:
        main.output = session["salida"]
    if request.method == "POST":
        entrada = request.form["entrada"]
        main = g.parse(entrada)
        main.input = entrada
        main.execute()
        session["entrada"] = entrada
        session["salida"] = main.output
    return render_template('index.html', entrada=entrada, text=main.output)

@app.route("/tree")
def tree():
    main = Global()
    image = ''
    if 'entrada' in session:
        main = g.parse(session["entrada"])
        main.graphTree()
        image = main.getGraph()
    return render_template('syntax-tree.html', image=image)

@app.route("/")
def index():
    return redirect("Compile")

if __name__ == '__main__':
    app.run(debug=True)
