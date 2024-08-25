from flask import Flask, render_template, request, redirect, url_for;
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template("index.html")

#Pelicula
@app.route('/indexPelicula')
def pelicula():
    
    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = "SELECT * FROM pelicula"
    cur.execute(Comando)
    pelicula = cur.fetchall()
    return render_template("pelicula/index.html",pelicula=pelicula)

#Capa
@app.route('/capa')
def capa():

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = "SELECT * FROM capa"	
    cur.execute(Comando)
    capa = cur.fetchall()
    return render_template("capa/index.html",capa=capa)

#Carregador
@app.route('/carregador')
def carregador():

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = "SELECT * FROM carregador"
    cur.execute(Comando)
    carregador = cur.fetchall()
    return render_template("carregador/index.html",carregador=carregador)

#Cabo_adaptador
@app.route('/cabo_adaptador')
def cabo_adaptador():

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = "SELECT * FROM cabos_adaptador"
    cur.execute(Comando)
    cabo_adaptador = cur.fetchall()
    return render_template("cabo_adaptador/index.html",cabo_adaptador=cabo_adaptador)

#Fone
@app.route('/fone')
def fone():
    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = "SELECT * FROM fone"
    cur.execute(Comando)
    fone = cur.fetchall()
    return render_template("fone/index.html",fone=fone)

@app.route('/Venda')
def Venda():
    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando_pelicula = "SELECT * FROM pelicula"
    Comando_capa = "SELECT * FROM capa"
    Comando_fone = "SELECT * FROM fone"
    Comando_carregador = "SELECT * FROM carregador"
    Comando_cabos_adaptador = "SELECT * FROM cabos_adaptador"
    
    cur.execute(Comando_pelicula)
    dados_pelicula = cur.fetchall()
    
    cur.execute(Comando_capa)
    dados_capa = cur.fetchall()

    cur.execute(Comando_cabos_adaptador)
    dados_cabos_adaptador = cur.fetchall()
    
    cur.execute(Comando_fone)
    dados_fone = cur.fetchall()
    
    cur.execute(Comando_carregador)
    dados_carregador = cur.fetchall()
    
    return render_template("Venda/index.html", dados=[dados_pelicula, dados_capa, dados_cabos_adaptador, dados_fone, dados_carregador])

if __name__ == '__main__':
  app.run(debug=True)
