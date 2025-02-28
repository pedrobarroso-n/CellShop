import os
import shutil
import sqlite3
import tempfile
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

# Caminho do banco de dados original e temporário
ORIGINAL_DB_PATH = 'Db.sql'

# Usar diretório temporário adequado para o sistema operacional
TEMP_DB_PATH = os.path.join(tempfile.gettempdir(), 'Db.sql')

# Verificar se o banco de dados já está na pasta temporária e copiá-lo se necessário
if not os.path.exists(TEMP_DB_PATH):
    shutil.copy(ORIGINAL_DB_PATH, TEMP_DB_PATH)


# Pagina Inicial
@app.route('/')
def index():
    return render_template("index.html")

# Cadastro
@app.route('/cadastro')
def cadastro():
    return render_template("cadastro/index.html")

# Buscar
@app.route('/buscar')
def buscar():
    return render_template("buscar/index.html")

# Resultados de busca
@app.route('/buscarItem', methods=['POST'])
def buscarItem():

    buscar = request.form.get('buscar')

    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    Comando_pelicula = f"SELECT * FROM pelicula WHERE modelo LIKE '%{buscar}%' COLLATE NOCASE"
    Comando_capa = f"SELECT * FROM capa WHERE modelo LIKE '%{buscar}%' COLLATE NOCASE"
    Comando_fone = f"SELECT * FROM fone WHERE modelo LIKE '%{buscar}%' COLLATE NOCASE"
    Comando_carregador = f"SELECT * FROM carregador WHERE tipo LIKE '%{buscar}%' COLLATE NOCASE"
    Comando_cabos_adaptador = f"SELECT * FROM cabos_adaptador WHERE entrada LIKE '%{buscar}%' COLLATE NOCASE"
    
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
    return render_template("buscar/result.html", dados=[dados_pelicula, dados_capa, dados_cabos_adaptador, dados_fone, dados_carregador])


# Pelicula
@app.route('/peliculas')
def pelicula():
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    Comando = "SELECT * FROM pelicula"
    cur.execute(Comando)
    pelicula = cur.fetchall()

    conn.close()
    return render_template("pelicula/index.html",pelicula=pelicula)

# Pelicula Vendas
@app.route('/vendasPelicula/<int:idpelicula>')
def vendasPelicula(idpelicula):
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    cur.execute('''
            UPDATE pelicula SET qtd = qtd - 1 
            WHERE idPelicula = ? AND qtd > 0
        ''', (idpelicula,))
    
    conn.commit()
    conn.close()
    return redirect('/peliculas')

# Pelicula Cadastro
@app.route('/add_pelicula', methods=['POST'])
def add_pelicula():
    modelo = request.form['modelo']
    tipo = request.form['tipo']
    img = request.form['img']
    preco = request.form['preco']
    qtd = request.form['qtd']

    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    cur.execute('''
            INSERT INTO pelicula (modelo, tipo, img, preco, qtd) VALUES (?,?,?,?,?)
        ''', (modelo, tipo, img, preco, qtd,))
    
    conn.commit()
    conn.close()
    return redirect('/cadastro')

# Capa
@app.route('/capas')
def capa():
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    Comando = "SELECT * FROM capa"    
    cur.execute(Comando)
    capa = cur.fetchall()
    
    conn.close()
    return render_template("capa/index.html",capa=capa)

# Capa Vendas
@app.route('/vendasCapa/<int:idcapa>')
def vendasCapa(idcapa):
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        UPDATE capa SET qtd = qtd - 1 
        WHERE idCP = ? AND qtd > 0
    ''', (idcapa,))

    conn.commit()
    conn.close()
    return redirect('/capas')

# Capa Cadastro
@app.route('/add_capa', methods=['POST'])
def add_capa():
    modelo = request.form['modelo']
    material = request.form['material']
    cor = request.form['cor']
    img = request.form['img']
    preco = request.form['preco']
    qtd = request.form['qtd']

    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    cur.execute('''
            INSERT INTO capa (modelo, material, cor, img, preco, qtd) VALUES (?,?,?,?,?,?)
        ''', (modelo, material, cor, img, preco, qtd,))
    
    conn.commit()
    conn.close()
    return redirect('/cadastro')

# Carregador
@app.route('/carregadores')
def carregador():
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    Comando = "SELECT * FROM carregador"
    cur.execute(Comando)
    carregador = cur.fetchall()

    conn.close()
    return render_template("carregador/index.html",carregador=carregador)

# Carregador Vendas
@app.route('/vendasCarregador/<int:idcarregador>')
def vendasCarregador(idcarregador):
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        UPDATE carregador SET qtd = qtd - 1 
        WHERE idCarregador = ? AND qtd > 0
    ''', (idcarregador,))

    conn.commit()
    conn.close()
    return redirect('/carregadores')

# Carregador Cadastro
@app.route('/add_carregador', methods=['POST'])
def add_carregador():
    cor = request.form['cor']
    tipo = request.form['tipo']
    img = request.form['img']
    preco = request.form['preco']
    qtd = request.form['qtd']

    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    cur.execute('''
            INSERT INTO carregador (cor, tipo, img, preco, qtd) VALUES (?,?,?,?,?)
        ''', (cor, tipo, img, preco, qtd,))
    
    conn.commit()
    conn.close()
    return redirect('/cadastro')

# Cabos_adaptador
@app.route('/cabos_adaptadores')
def cabo_adaptador():
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    Comando = "SELECT * FROM cabos_adaptador"
    cur.execute(Comando)
    cabo_adaptador = cur.fetchall()

    conn.close()
    return render_template("cabo_adaptador/index.html",cabo_adaptador=cabo_adaptador)

# Cabos_adaptador Vendas
@app.route('/vendasCabos_adaptador/<int:idcabo>')
def vendasCabos_adaptador(idcabo):
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        UPDATE cabos_adaptador SET qtd = qtd - 1 
        WHERE idCabo = ? AND qtd > 0
    ''', (idcabo,))

    conn.commit()
    conn.close()
    return redirect('/cabos_adaptadores')

# Cabos_adaptador Cadastro
@app.route('/add_cabos_adaptador', methods=['POST'])
def add_cabos_adaptador():
    entrada = request.form['entrada']
    saida = request.form['saida']
    tipo = request.form['tipo']
    img = request.form['img']
    preco = request.form['preco']
    qtd = request.form['qtd']

    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    cur.execute('''
            INSERT INTO cabos_adaptador (entrada, saida, tipo, img, preco, qtd) VALUES (?,?,?,?,?,?)
        ''', (entrada, saida, tipo, img, preco, qtd,))
    
    conn.commit()
    conn.close()
    return redirect('/cadastro')

# Fone
@app.route('/fones')
def fone():
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    Comando = "SELECT * FROM fone"
    cur.execute(Comando)
    fone = cur.fetchall()

    conn.close()
    return render_template("fone/index.html",fone=fone)

# Fone Vendas
@app.route('/vendasFone/<int:idfone>')
def vendasFone(idfone):
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        UPDATE fone SET qtd = qtd - 1 
        WHERE idFone = ? AND qtd > 0
    ''', (idfone,))

    conn.commit()
    conn.close()
    return redirect('/fones')

# Fone Cadastro
@app.route('/add_fone', methods=['POST'])
def add_fone():
    modelo = request.form['modelo']
    marca = request.form['marca']
    tipo = request.form['tipo']
    img = request.form['img']
    preco = request.form['preco']
    qtd = request.form['qtd']

    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    cur.execute('''
            INSERT INTO fone (modelo, marca, tipo, img, preco, qtd) VALUES (?,?,?,?,?,?)
        ''', (modelo, marca, tipo, img, preco, qtd,))
    
    conn.commit()
    conn.close()
    return redirect('/cadastro')

# Compra Pelicula
@app.route('/compraPelicula/<int:id>')
def compraPelicula(id):
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    Comando = f"SELECT * FROM pelicula WHERE idPelicula = {id}"
    cur.execute(Comando)
    compra = cur.fetchall()
   
    conn.close()
    return render_template("compraPelicula/index.html", compra=compra)

# Compra Capa
@app.route('/compraCapa/<int:id>')
def compraCapa(id):
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    Comando = f"SELECT * FROM capa WHERE idCP = {id}"
    cur.execute(Comando)
    compra = cur.fetchall()
   
    conn.close()
    return render_template("compraCapa/index.html", compra=compra)

# Compra Carregador
@app.route('/compraCarregador/<int:id>')
def compraCarregador(id):
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    Comando = f"SELECT * FROM carregador WHERE idCarregador = {id}"
    cur.execute(Comando)
    compra = cur.fetchall()
   
    conn.close()
    return render_template("compraCarregador/index.html", compra=compra)

# Compra Fone
@app.route('/compraFone/<int:id>')
def compraFone(id):
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    Comando = f"SELECT * FROM fone WHERE idFone= {id}"
    cur.execute(Comando)
    compra = cur.fetchall()
   
    conn.close()
    return render_template("compraFone/index.html", compra=compra)

# Compra Cabos_adaptador
@app.route('/compraCabos_adaptador/<int:id>')
def compraCabos_adaptador(id):
    conn = sqlite3.connect(TEMP_DB_PATH)
    cur = conn.cursor()
    Comando = f"SELECT * FROM cabos_adaptador WHERE idCabo= {id}"
    cur.execute(Comando)
    compra = cur.fetchall()
   
    conn.close()
    return render_template("compraCabos_adaptador/index.html", compra=compra)







if __name__ == '__main__':
    app.secret_key = 'CellTop24'
    app.run(debug=True)
