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

