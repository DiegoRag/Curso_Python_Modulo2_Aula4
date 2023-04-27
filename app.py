#Comentario nova versao
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "aaaa"

@app.route("/produtos")
def produtos():
    return "Minha pagina de produtos"

@app.route("/sobre")
def sobre():
    return "Curso muito bem do bom"

if __name__ == "__main__":
    app.run(debug=True)