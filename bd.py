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
    ('iPhone 13', 'Vidro Temperado', 'img1.jpg', 29.99, 50),
    ('Samsung S21', 'Vidro Temperado', 'img2.jpg', 24.99, 30),
    ('Xiaomi Mi 11', 'Plástico', 'img3.jpg', 19.99, 40),
    ('Google Pixel 5', 'Vidro Temperado', 'img4.jpg', 22.50, 20),
    ('OnePlus 9', 'Plástico', 'img5.jpg', 18.99, 15),
    ('iPhone 12', 'Vidro Temperado', 'img6.jpg', 27.99, 25),
    ('Samsung S20', 'Vidro Temperado', 'img7.jpg', 23.99, 10),
    ('Xiaomi Mi 10', 'Plástico', 'img8.jpg', 17.99, 12),
    ('Google Pixel 4a', 'Vidro Temperado', 'img9.jpg', 20.99, 18),
    ('OnePlus 8T', 'Vidro Temperado', 'img10.jpg', 25.99, 22)
]

inserirCapa = """
INSERT INTO capa (modelo, cor, material, img, preco, qtd) VALUES (? ,? ,? ,? ,? ,?);

"""
dadosCapa = [

    ('iPhone 13', 'Preto', 'Silicone', 'img1.jpg', 39.99, 30),
    ('Samsung S21', 'Azul', 'Couro', 'img2.jpg', 49.99, 20),
    ('Xiaomi Mi 11', 'Vermelho', 'Plástico', 'img3.jpg', 29.99, 50),
    ('Google Pixel 5', 'Verde', 'Tecido', 'img4.jpg', 34.50, 15),
    ('OnePlus 9', 'Branco', 'Silicone', 'img5.jpg', 44.99, 25),
    ('iPhone 12', 'Preto', 'Couro', 'img6.jpg', 45.99, 10),
    ('Samsung S20', 'Amarelo', 'Plástico', 'img7.jpg', 24.99, 35),
    ('Xiaomi Mi 10', 'Cinza', 'Silicone', 'img8.jpg', 31.99, 12),
    ('Google Pixel 4a', 'Rosa', 'Tecido', 'img9.jpg', 39.99, 18),
    ('OnePlus 8T', 'Azul', 'Couro', 'img10.jpg', 49.99, 20)
]

inserirCarregador = """
INSERT INTO carregador (tipo, cor, img, preco, qtd) VALUES (?,?,?,?,?);
"""
dadosCarregador = [
    ('USB-C', 'Branco', 'img1.jpg', 29.99, 50),
    ('Micro-USB', 'Preto', 'img2.jpg', 19.99, 40),
    ('Lightning', 'Branco', 'img3.jpg', 24.99, 30),
    ('USB-C', 'Preto', 'img4.jpg', 28.50, 20),
    ('Micro-USB', 'Azul', 'img5.jpg', 17.99, 15),
    ('Lightning', 'Preto', 'img6.jpg', 25.99, 25),
    ('USB-C', 'Vermelho', 'img7.jpg', 27.99, 10),
    ('Micro-USB', 'Branco', 'img8.jpg', 18.99, 12),
    ('Lightning', 'Cinza', 'img9.jpg', 22.99, 18),
    ('USB-C', 'Verde', 'img10.jpg', 26.99, 22)
]

inserirCabos_adaptador = """
INSERT INTO cabos_adaptador (tipo, entrada, saida, img, preco, qtd) VALUES
(?, ?, ?, ?, ?, ?);

"""
dadosCabos_adaptador = [

    ('Cabo', 'USB-C', 'HDMI', 'img1.jpg', 15.99, 30),
    ('Adaptador', 'Micro-USB', 'USB-A', 'img2.jpg', 9.99, 20),
    ('Cabo', 'Lightning', 'USB-C', 'img3.jpg', 19.99, 40),
    ('Adaptador', 'USB-C', 'VGA', 'img4.jpg', 12.50, 15),
    ('Cabo', 'Micro-USB', 'HDMI', 'img5.jpg', 14.99, 25),
    ('Adaptador', 'Lightning', 'USB-A', 'img6.jpg', 11.99, 10),
    ('Cabo', 'USB-C', 'Ethernet', 'img7.jpg', 16.99, 35),
    ('Adaptador', 'Micro-USB', 'Ethernet', 'img8.jpg', 13.99, 12),
    ('Cabo', 'Lightning', 'HDMI', 'img9.jpg', 21.99, 18),
    ('Adaptador', 'USB-C', 'DisplayPort', 'img10.jpg', 17.99, 22)
]

inserirFone = """
INSERT INTO fone (modelo, tipo, marca, img, preco, qtd) VALUES 
(?,?,?,?,?,?);
"""

dadosFone = [
    ('AirPods Pro', 'Bluetooth', 'Apple', 'img1.jpg', 249.99, 50),
    ('Galaxy Buds', 'Bluetooth', 'Samsung', 'img2.jpg', 199.99, 40),
    ('Mi True Wireless', 'Bluetooth', 'Xiaomi', 'img3.jpg', 99.99, 30),
    ('Pixel Buds', 'Bluetooth', 'Google', 'img4.jpg', 179.50, 20),
    ('OnePlus Buds', 'Bluetooth', 'OnePlus', 'img5.jpg', 149.99, 15),
    ('AirPods 2', 'Bluetooth', 'Apple', 'img6.jpg', 199.99, 25),
    ('Galaxy Buds Live', 'Bluetooth', 'Samsung', 'img7.jpg', 229.99, 10),
    ('Redmi Buds', 'Bluetooth', 'Xiaomi', 'img8.jpg', 89.99, 12),
    ('Pixel Buds A', 'Bluetooth', 'Google', 'img9.jpg', 129.99, 18),
    ('OnePlus Buds Z', 'Bluetooth', 'OnePlus', 'img10.jpg', 119.99, 22)
]


cur.executemany(inserirPelicula,dadosPelicula)
cur.executemany(inserirCapa,dadosCapa)
cur.executemany(inserirCarregador,dadosCarregador)
cur.executemany(inserirCabos_adaptador, dadosCabos_adaptador)
cur.executemany(inserirFone, dadosFone)
conn.commit()

