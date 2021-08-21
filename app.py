import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash

# Configuração
DATABASE = "blog.db"
SECRET_KEY = 'pudim'


app = Flask(__name__) # faz tudo: cria o servidor
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

@app.route("/")

def pagina_inicial():
    return "<input autofocus></input>"
    

