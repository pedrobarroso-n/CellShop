import sqlite3
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


#Pelicula
@app.route('/peliculas')
def pelicula():
    
    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = "SELECT * FROM pelicula"
    cur.execute(Comando)
    pelicula = cur.fetchall()

    conn.close()
    return render_template("pelicula/index.html",pelicula=pelicula)


#Capa
@app.route('/capas')
def capa():

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = "SELECT * FROM capa"	
    cur.execute(Comando)
    capa = cur.fetchall()
    
    conn.close()
    return render_template("capa/index.html",capa=capa)


#Carregador
@app.route('/carregadores')
def carregador():

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = "SELECT * FROM carregador"
    cur.execute(Comando)
    carregador = cur.fetchall()

    conn.close()
    return render_template("carregador/index.html",carregador=carregador)


#Cabos_adaptador
@app.route('/cabos_adaptadores')
def cabo_adaptador():

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = "SELECT * FROM cabos_adaptador"
    cur.execute(Comando)
    cabo_adaptador = cur.fetchall()

    conn.close()
    return render_template("cabo_adaptador/index.html",cabo_adaptador=cabo_adaptador)


#Fone
@app.route('/fones')
def fone():
    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = "SELECT * FROM fone"
    cur.execute(Comando)
    fone = cur.fetchall()
    conn.close()
    return render_template("fone/index.html",fone=fone)


if __name__ == '__main__':
    app.secret_key = 'TudoANos'
    app.run(debug=True)


