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

#Capa2
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

#Cabo_adaptador
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

#Venda
@app.route('/Vendas')
def Vendas():
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
    
    conn.close()
    return render_template("Venda/index.html", dados=[dados_pelicula, dados_capa, dados_cabos_adaptador,dados_fone,dados_carregador])


@app.route('/Venda_pelicula', methods=['GET', 'POST'])
def Venda_pelicula():
    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    if request.method == "GET":
        conn.close()
        return redirect("/Vendas")
    elif request.method == "POST":

        """
        0 - idPelicula
        1 - modelo
        2 - tipo
        3 - img
        4 - preco
        5 - qtd
        """
        qtd_Compra = request.form['qtd']
        qtd_Compra = int(qtd_Compra)
        dado = request.form['dados'].replace("'","").replace(" ","")
        DadosLista = dado.split(",")
        DadosLista[0] = int(DadosLista[0])
        DadosLista[4] = float(DadosLista[4])
        DadosLista[5]  = int(DadosLista[5])
        
        atualizarQtd = "UPDATE pelicula SET qtd = qtd - ? WHERE idPelicula = ?"
        if qtd_Compra <= DadosLista[5] or qtd_Compra >= DadosLista[5]:
            pass
        else:
            cur.execute(atualizarQtd, (DadosLista[5], DadosLista[0]))
            conn.commit()
            conn.close()
        
        return redirect("/Vendas")

@app.route('/Venda_capa', methods=['GET', 'POST'])
def Venda_capa():
    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    if request.method == "GET":
        conn.close()
        return redirect("/Vendas")
    elif request.method == "POST": 
        """
        0 - idCP
        1 - modelo
        2 - cor
        3 - material
        4 - img
        5 - preco
        6 - qtd
        """
        qtd_Compra = request.form['qtd']
        qtd_Compra = int(qtd_Compra)
        dado = request.form['dados'].replace("'","").replace(" ","")
        DadosLista = dado.split(",")
        DadosLista[0] = int(DadosLista[0])
        DadosLista[5] = float(DadosLista[5])
        DadosLista[6]  = int(DadosLista[6])

        atualizarQtd = "updade capa SET qtd = qtd - ? WHERE idCapa = ?"
        if qtd_Compra <= DadosLista[6] or qtd_Compra >= DadosLista[6]:
            pass
        else:
            print(DadosLista)
            cur.execute(atualizarQtd, (DadosLista[6], DadosLista[0]))
            conn.commit()
            conn.close()

        return redirect("/Vendas")




if __name__ == '__main__':
    app.secret_key = 'TudoANos'
    app.run(debug=True)
