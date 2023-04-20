from flask import Flask

app = Flask(__name__)

@app.route("/")
def curso():
    return "curso de python turma dois bem bom"

@app.route("/produtos")
def produtos():
    return "Minha pagina de produtos"

@app.route("/sobre")
def sobre():
    return "Curso muito bem do bom"

