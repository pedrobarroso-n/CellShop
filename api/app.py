import sqlite3
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

#Home Page
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


#Pelicula Vendas
@app.route('/vendasPelicula/<int:idpelicula>')
def vendasPelicula(idpelicula):

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    cur.execute('''
        UPDATE pelicula SET qtd = qtd - 1 
        WHERE idPelicula = ? AND qtd > 0
    ''', (idpelicula,))

    conn.commit()

    conn.close()
    return redirect('/peliculas')


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


#Capa Vendas
@app.route('/vendasCapa/<int:idcapa>')
def vendasCapa(idcapa):

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    cur.execute('''
        UPDATE capa SET qtd = qtd - 1 
        WHERE idCP = ? AND qtd > 0
    ''', (idcapa,))

    conn.commit()
    conn.close()
    return redirect('/capas')


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


#Carregador Vendas
@app.route('/vendasCarregador/<int:idcarregador>')
def vendasCarregador(idcarregador):

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    cur.execute('''
        UPDATE carregador SET qtd = qtd - 1 
        WHERE idCarregador = ? AND qtd > 0
    ''', (idcarregador,))

    conn.commit()
    conn.close()
    return redirect('/carregadores')


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


#Cabos_adaptador Vendas
@app.route('/vendasCabos_adaptador/<int:idcabo>')
def vendasCabos_adaptador(idcabo):

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    cur.execute('''
        UPDATE cabos_adaptador SET qtd = qtd - 1 
        WHERE idCabo = ? AND qtd > 0
    ''', (idcabo,))

    conn.commit()
    conn.close()
    return redirect('/cabos_adaptadores')


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


#Fone Vendas
@app.route('/vendasFone/<int:idfone>')
def vendasFone(idfone):

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    cur.execute('''
        UPDATE fone SET qtd = qtd - 1 
        WHERE idFone = ? AND qtd > 0
    ''', (idfone,))

    conn.commit()
    conn.close()
    return redirect('/fones')


#Compra Pelicula
@app.route('/compraPelicula/<int:id>')
def compraPelicula(id):

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = f"SELECT * FROM pelicula WHERE idPelicula = {id}"
    cur.execute(Comando)
    compra = cur.fetchall()
   
    conn.close()
    return render_template("compraPelicula/index.html", compra=compra)


#Compra Capa
@app.route('/compraCapa/<int:id>')
def compraCapa(id):

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = f"SELECT * FROM capa WHERE idCP = {id}"
    cur.execute(Comando)
    compra = cur.fetchall()
   
    conn.close()
    return render_template("compraCapa/index.html", compra=compra)


#Compra Carregador
@app.route('/compraCarregador/<int:id>')
def compraCarregador(id):

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = f"SELECT * FROM carregador WHERE idCarregador = {id}"
    cur.execute(Comando)
    compra = cur.fetchall()
   
    conn.close()
    return render_template("compraCarregador/index.html", compra=compra)


#Compra Fone
@app.route('/compraFone/<int:id>')
def compraFone(id):

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = f"SELECT * FROM fone WHERE idFone= {id}"
    cur.execute(Comando)
    compra = cur.fetchall()
   
    conn.close()
    return render_template("compraFone/index.html", compra=compra)


#Compra Cabos_adaptador
@app.route('/compraCabos_adaptador/<int:id>')
def compraCabos_adaptador(id):

    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    Comando = f"SELECT * FROM cabos_adaptador WHERE idCabo= {id}"
    cur.execute(Comando)
    compra = cur.fetchall()
   
    conn.close()
    return render_template("compraCabos_adaptador/index.html", compra=compra)



if __name__ == '__main__':
    app.secret_key = 'CellTop24'
    app.run(debug=True)

