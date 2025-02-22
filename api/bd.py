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
conn.close()

