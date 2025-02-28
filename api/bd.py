import sqlite3 

conn = sqlite3.connect("Db.sql")
cur = conn.cursor()

#Tabelas
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


inserirPelicula = """
INSERT INTO pelicula (modelo, tipo, img, preco, qtd) VALUES (?,?,?,?,?);
"""
dadosPelicula = [
    ('iPhone 13', 'Vidro Temperado', '../../static/img/pelicula/pelicula1.webp', 29.99, 50),
    ('Samsung S21', 'Vidro Temperado', '../../static/img/pelicula/pelicula2.jpg', 24.99, 30),
    ('Xiaomi Mi 11', 'Plástico', '../../static/img/pelicula/pelicula3.webp', 19.99, 40),
    ('Google Pixel 5', 'Vidro Temperado', '../../static/img/pelicula/pelicula4.jpg', 22.50, 20),
    ('OnePlus 9', 'Plástico', '../../static/img/pelicula/pelicula5.webp', 18.99, 15),
]

inserirCapa = """
INSERT INTO capa (modelo, cor, material, img, preco, qtd) VALUES (?,?,?,?,?,?);
"""
dadosCapa = [

    ('iPhone 13', 'Preto', 'Silicone', '../../static/img/capa/capa1.webp', 39.99, 30),
    ('Samsung S21', 'Azul', 'Couro', '../../static/img/capa/capa2.webp', 49.99, 20),
    ('Xiaomi Mi 11', 'Vermelho', 'Plástico', '../../static/img/capa/capa3.webp', 29.99, 50),
    ('Google Pixel 5', 'Verde', 'Tecido', '../../static/img/capa/capa4.webp', 34.50, 15),
    ('OnePlus 9', 'Branco', 'Silicone', '../../static/img/capa/capa5.webp', 44.99, 25),
]

inserirCarregador = """
INSERT INTO carregador (tipo, cor, img, preco, qtd) VALUES (?,?,?,?,?);
"""
dadosCarregador = [
    ('USB-C', 'Branco', '../../static/img/carregador/carregador1.webp', 29.99, 50),
    ('Micro-USB', 'Preto', '../../static/img/carregador/carregador2.webp', 19.99, 40),
    ('Lightning', 'Branco', '../../static/img/carregador/carregador3.webp', 24.99, 30),
    ('USB-C', 'Preto', '../../static/img/carregador/carregador4.webp', 28.50, 20),
    ('Micro-USB', 'Azul', '../../static/img/carregador/carregador5.webp', 17.99, 15),
]

inserirCabos_adaptador = """
INSERT INTO cabos_adaptador (tipo, entrada, saida, img, preco, qtd) VALUES(?,?,?,?,?,?);
"""
dadosCabos_adaptador = [

    ('Cabo', 'USB-C', 'HDMI', '../../static/img/cabo_adaptador/cabo-adap1.webp', 15.99, 30),
    ('Adaptador', 'Micro-USB', 'USB-A', '../../static/img/cabo_adaptador/cabo-adap2.webp', 9.99, 20),
    ('Cabo', 'Lightning', 'USB-C', '../../static/img/cabo_adaptador/cabo-adap3.webp', 19.99, 40),
    ('Adaptador', 'USB-C', 'VGA', '../../static/img/cabo_adaptador/cabo-adap4.webp', 12.50, 15),
    ('Cabo', 'Micro-USB', 'HDMI', '../../static/img/cabo_adaptador/cabo-adap5.webp', 14.99, 25),
]

inserirFone = """
INSERT INTO fone (modelo, tipo, marca, img, preco, qtd) VALUES (?,?,?,?,?,?);
"""
dadosFone = [
    ('AirPods Pro', 'Bluetooth', 'Apple', '../../static/img/fone/fone1.webp', 249.99, 50),
    ('Galaxy Buds', 'Bluetooth', 'Samsung', '../../static/img/fone/fone2.webp', 199.99, 40),
    ('Mi True Wireless', 'Bluetooth', 'Xiaomi', '../../static/img/fone/fone3.webp', 99.99, 30),
    ('Pixel Buds', 'Bluetooth', 'Google', '../../static/img/fone/fone4.webp', 179.50, 20),
    ('OnePlus Buds', 'Bluetooth', 'OnePlus', '../../static/img/fone/fone5.webp', 149.99, 15),
]


def criarTabelas():
    cur.execute(pelicula)
    cur.execute(capa)
    cur.execute(carregador)
    cur.execute(cabos_adaptador)
    cur.execute(fone)

def apagarTudo():
    cur.execute('DELETE FROM pelicula WHERE idPelicula > 0;')
    cur.execute('DELETE FROM capa WHERE idCP > 0;')
    cur.execute('DELETE FROM carregador WHERE idCarregador > 0;')
    cur.execute('DELETE FROM cabos_adaptador WHERE idCabo > 0;')
    cur.execute('DELETE FROM fone WHERE idFone > 0;')

def adicionarDados():
    cur.executemany(inserirPelicula,dadosPelicula)
    cur.executemany(inserirCapa,dadosCapa)
    cur.executemany(inserirCarregador,dadosCarregador)
    cur.executemany(inserirCabos_adaptador, dadosCabos_adaptador)
    cur.executemany(inserirFone, dadosFone)


criarTabelas()
conn.commit()
conn.close()

