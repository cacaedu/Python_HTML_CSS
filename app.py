import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash

# Configuração
DATABASE = "blog.db"
SECRET_KEY = 'pudim'

app = Flask(__name__) # faz tudo: cria o servidor
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def antes_requisicao():    
    g.bd = conectar_bd()

@app.teardown_request
def depois_request(exc):
    g.bd.close()

@app.route("/")
def exibir_entradas():
    #return render_template("exibir_entradas.html", mensagem="Olá pessoas!!")
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto in cur.fetchall():
        entradas.append({'titulo': titulo, 'texto': texto})

    return render_template('exibir_entradas.html', entradas=entradas )

#@app.route("/hello")
#def pagina_inicial():
    #return "<h1 style='color: red'>Hello</h1>"

@app.route('/inserir')
def inserir_entrada():
    sql = "INSERT INTO entradas(titulo, texto) VALUES ('Terceiro post', 'Esse é o post')"
    g.bd.execute(sql)
    g.bd.commit()
    return redirect('/entradas')