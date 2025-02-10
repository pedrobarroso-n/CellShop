import sqlite3
from flask import Flask, render_template, request, url_for, redirect

conn = sqlite3.connect("Db.sql")
cur = conn.cursor()

#----------------------------| Tabelas |-----------------------------------------
pelicula = """
CREATE TABLE IF NOT EXISTS pelicula (
    idPelicula INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo VARCHAR(50),
    tipo VARCHAR(50),
    img VARCHAR(100),
    preco DECIMAL(5,2),
    qtd INTEGER
);
"""

capa = """
CREATE TABLE IF NOT EXISTS capa (
    idCP INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo VARCHAR(50),
    cor VARCHAR(25),
    material VARCHAR(50),
    img varchar(100),
    preco decimail(5,2),
    qtd inetger
);"""

carregador = """
CREATE TABLE IF NOT EXISTS carregador (
    idCarregador INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo VARCHAR(50),
    cor VARCHAR(25),
    img varchar(100),
    preco decimail(5,2),
    qtd inetger
);"""

cabos_adaptador = """
CREATE TABLE IF NOT EXISTS cabos_adaptador (
    idCabo INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo VARCHAR(50),
    entrada VARCHAR(50),
    saida VARCHAR(50),
    img varchar(100),
    preco decimail(5,2),
    qtd inetger
);
"""
fone = """
CREATE TABLE IF NOT EXISTS fone (
    idFone INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo VARCHAR(50),
    tipo VARCHAR(50),
    marca VARCHAR(50),
    img varchar(100),
    preco decimail(5,2),
    qtd inetger
);
"""
cur.execute(pelicula)
cur.execute(capa)
cur.execute(carregador)
cur.execute(cabos_adaptador)
cur.execute(fone)
conn.commit()

#Dados ficticios
inserirPelicula = """
INSERT INTO pelicula (modelo, tipo, img, preco, qtd) VALUES (?,?,?,?,?);
"""
dadosPelicula = [
    ('iPhone 13', 'Vidro Temperado', 'pelicula1.webp', 29.99, 50),
    ('Samsung S21', 'Vidro Temperado', 'pelicula2.jpg', 24.99, 30),
    ('Xiaomi Mi 11', 'Plástico', 'pelicula3.webp', 19.99, 40),
    ('Google Pixel 5', 'Vidro Temperado', 'pelicula4.jpg', 22.50, 20),
    ('OnePlus 9', 'Plástico', 'pelicula5.webp', 18.99, 15),
    ('iPhone 12', 'Vidro Temperado', 'pelicula1.webp', 27.99, 25),
    ('Samsung S20', 'Vidro Temperado', 'pelicula2.jpg', 23.99, 10),
    ('Xiaomi Mi 10', 'Plástico', 'pelicula3.webp', 17.99, 12),
    ('Google Pixel 4a', 'Vidro Temperado', 'pelicula4.jpg', 20.99, 18),
    ('OnePlus 8T', 'Vidro Temperado', 'pelicula5.webp', 25.99, 22)
]

inserirCapa = """
INSERT INTO capa (modelo, cor, material, img, preco, qtd) VALUES (? ,? ,? ,? ,? ,?);

"""
dadosCapa = [

    ('iPhone 13', 'Preto', 'Silicone', 'capa1.webp', 39.99, 30),
    ('Samsung S21', 'Azul', 'Couro', 'capa2.webp', 49.99, 20),
    ('Xiaomi Mi 11', 'Vermelho', 'Plástico', 'capa3.webp', 29.99, 50),
    ('Google Pixel 5', 'Verde', 'Tecido', 'capa4.webp', 34.50, 15),
    ('OnePlus 9', 'Branco', 'Silicone', 'capa1.webp', 44.99, 25),
    ('iPhone 12', 'Preto', 'Couro', 'capa2.webp', 45.99, 10),
    ('Samsung S20', 'Amarelo', 'Plástico', 'capa3.webp', 24.99, 35),
    ('Xiaomi Mi 10', 'Cinza', 'Silicone', 'capa4.webp', 31.99, 12),
    ('Google Pixel 4a', 'Rosa', 'Tecido', 'capa1.webp', 39.99, 18),
    ('OnePlus 8T', 'Azul', 'Couro', 'capa2.webp', 49.99, 20)
]

inserirCarregador = """
INSERT INTO carregador (tipo, cor, img, preco, qtd) VALUES (?,?,?,?,?);
"""
dadosCarregador = [
    ('USB-C', 'Branco', 'carregador1.webp', 29.99, 50),
    ('Micro-USB', 'Preto', 'carregador2.webp', 19.99, 40),
    ('Lightning', 'Branco', 'carregador3.webp', 24.99, 30),
    ('USB-C', 'Preto', 'carregador4.webp', 28.50, 20),
    ('Micro-USB', 'Azul', 'carregador5.webp', 17.99, 15),
    ('Lightning', 'Preto', 'carregador6.webp', 25.99, 25),
    ('USB-C', 'Vermelho', 'carregador7.webp', 27.99, 10),
    ('Micro-USB', 'Branco', 'carregador1.webp', 18.99, 12),
    ('Lightning', 'Cinza', 'carregador2.webp', 22.99, 18),
    ('USB-C', 'Verde', 'carregador3.webp', 26.99, 22)
]

inserirCabos_adaptador = """
INSERT INTO cabos_adaptador (tipo, entrada, saida, img, preco, qtd) VALUES
(?, ?, ?, ?, ?, ?);

"""
dadosCabos_adaptador = [

    ('Cabo', 'USB-C', 'HDMI', 'cabo-adap1.webp', 15.99, 30),
    ('Adaptador', 'Micro-USB', 'USB-A', 'cabo-adap2.webp', 9.99, 20),
    ('Cabo', 'Lightning', 'USB-C', 'cabo-adap3.webp', 19.99, 40),
    ('Adaptador', 'USB-C', 'VGA', 'cabo-adap4.webp', 12.50, 15),
    ('Cabo', 'Micro-USB', 'HDMI', 'cabo-adap5.webp', 14.99, 25),
    ('Adaptador', 'Lightning', 'USB-A', 'cabo-adap1.webp', 11.99, 10),
    ('Cabo', 'USB-C', 'Ethernet', 'cabo-adap2.webp', 16.99, 35),
    ('Adaptador', 'Micro-USB', 'Ethernet', 'cabo-adap3.webp', 13.99, 12),
    ('Cabo', 'Lightning', 'HDMI', 'cabo-adap4.webp', 21.99, 18),
    ('Adaptador', 'USB-C', 'DisplayPort', 'cabo-adap5.webp', 17.99, 22)
]

inserirFone = """
INSERT INTO fone (modelo, tipo, marca, img, preco, qtd) VALUES 
(?,?,?,?,?,?);
"""

dadosFone = [
    ('AirPods Pro', 'Bluetooth', 'Apple', 'fone1.webp', 249.99, 50),
    ('Galaxy Buds', 'Bluetooth', 'Samsung', 'fone2.webp', 199.99, 40),
    ('Mi True Wireless', 'Bluetooth', 'Xiaomi', 'fone3.webp', 99.99, 30),
    ('Pixel Buds', 'Bluetooth', 'Google', 'fone4.webp', 179.50, 20),
    ('OnePlus Buds', 'Bluetooth', 'OnePlus', 'fone5.webp', 149.99, 15),
    ('AirPods 2', 'Bluetooth', 'Apple', 'fone6.webp', 199.99, 25),
    ('Galaxy Buds Live', 'Bluetooth', 'Samsung', 'fone7.webp', 229.99, 10),
    ('Redmi Buds', 'Bluetooth', 'Xiaomi', 'fone8.webp', 89.99, 12),
    ('Pixel Buds A', 'Bluetooth', 'Google', 'fone9.webp', 129.99, 18),
    ('OnePlus Buds Z', 'Bluetooth', 'OnePlus', 'fone1.webp', 119.99, 22)
]


cur.executemany(inserirPelicula,dadosPelicula)
cur.executemany(inserirCapa,dadosCapa)
cur.executemany(inserirCarregador,dadosCarregador)
cur.executemany(inserirCabos_adaptador, dadosCabos_adaptador)
cur.executemany(inserirFone, dadosFone)
conn.commit()

#-----------------------------------| APP |-----------------------------------------

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


@app.route('/Venda_fone', methods=['GET', 'POST'])
def Venda_fone():
    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    if request.method == "GET":
        conn.close()
        return redirect("/Vendas")
    elif request.method == "POST": 
        
        qtd_Compra = request.form['qtd']
        qtd_Compra = int(qtd_Compra)
        dado = request.form['dados'].replace("'","").replace(" ","")
        DadosLista = dado.split(",")
        DadosLista[0] = int(DadosLista[0])
        DadosLista[5] = float(DadosLista[5])
        DadosLista[6]  = int(DadosLista[6])

        atualizarQtd = "updade fone SET qtd = qtd - ? WHERE idFone = ?"
        if qtd_Compra <= DadosLista[6] or qtd_Compra >= DadosLista[6]:
            pass
        else:
            print(DadosLista)
            cur.execute(atualizarQtd, (DadosLista[6], DadosLista[0]))
            conn.commit()
            conn.close()

        return redirect("/Vendas")


@app.route('/Venda_carregador', methods=['GET', 'POST'])
def Venda_carregador():
    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    if request.method == "GET":
        conn.close()
        return redirect("/Vendas")
    elif request.method == "POST": 

        qtd_Compra = request.form['qtd']
        qtd_Compra = int(qtd_Compra)
        dado = request.form['dados'].replace("'","").replace(" ","")
        DadosLista = dado.split(",")
        DadosLista[0] = int(DadosLista[0])
        DadosLista[5] = float(DadosLista[5])
        DadosLista[6]  = int(DadosLista[6])

        atualizarQtd = "updade carregador SET qtd = qtd - ? WHERE idCarregador = ?"
        if qtd_Compra <= DadosLista[6] or qtd_Compra >= DadosLista[6]:
            pass
        else:
            print(DadosLista)
            cur.execute(atualizarQtd, (DadosLista[6], DadosLista[0]))
            conn.commit()
            conn.close()

        return redirect("/Vendas")


@app.route('/Venda_cabos_adaptador', methods=['GET', 'POST'])
def Venda_cabos_adaptador():
    conn = sqlite3.connect('Db.sql')
    cur = conn.cursor()
    if request.method == "GET":
        conn.close()
        return redirect("/Vendas")
    elif request.method == "POST": 
        
        qtd_Compra = request.form['qtd']
        qtd_Compra = int(qtd_Compra)
        dado = request.form['dados'].replace("'","").replace(" ","")
        DadosLista = dado.split(",")
        DadosLista[0] = int(DadosLista[0])
        DadosLista[5] = float(DadosLista[5])
        DadosLista[6]  = int(DadosLista[6])

        atualizarQtd = "updade cabos_adaptador SET qts = qtd - ? WHERE idCabo = ?"
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


