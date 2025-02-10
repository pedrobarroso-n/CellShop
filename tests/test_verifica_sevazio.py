import pytest
import sqlite3

@pytest.fixture
def conexao():
    """Cria um banco de dados temporário em memória para testes."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Criando a tabela 'fone' com campos NOT NULL
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fone (
            idFone INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            tipo TEXT NOT NULL,
            marca TEXT NOT NULL,
            img TEXT,
            preco REAL NOT NULL,
            qtd INTEGER NOT NULL
        )
    """)

    # Inserindo alguns itens fictícios na tabela 'fone'
    cursor.executemany("""
        INSERT INTO fone (modelo, tipo, marca, img, preco, qtd)
        VALUES (?, ?, ?, ?, ?, ?)
    """, [
        ('Fone 1', 'Bluetooth', 'Marca A', 'img1.jpg', 199.99, 10),
        ('Fone 2', 'Com fio', 'Marca B', 'img2.jpg', 99.99, 20),
        ('Fone 3', 'Bluetooth', 'Marca C', 'img3.jpg', 149.99, 15)
    ])
    conn.commit()

    yield conn  # Retorna a conexão para ser usada nos testes
    conn.close()

def test_campos_not_null(conexao):
    """Verifica se todos os campos NOT NULL da tabela 'fone' têm dados válidos (não nulos) e salva os resultados."""
    resultado_teste = []  # Lista para armazenar os resultados do teste
    cursor = conexao.cursor()

    # Recupera todos os itens da tabela 'fone'
    cursor.execute("SELECT * FROM fone")
    itens_fone = cursor.fetchall()

    # Verifica se todos os campos NOT NULL não são NULL
    for item in itens_fone:
        idFone, modelo, tipo, marca, img, preco, qtd = item

        modelo_check = modelo is not None
        tipo_check = tipo is not None
        marca_check = marca is not None
        preco_check = preco is not None
        qtd_check = qtd is not None

        resultado_teste.append(f"ID {idFone} - Modelo: {'PASS' if modelo_check else 'FAIL'}")
        resultado_teste.append(f"ID {idFone} - Tipo: {'PASS' if tipo_check else 'FAIL'}")
        resultado_teste.append(f"ID {idFone} - Marca: {'PASS' if marca_check else 'FAIL'}")
        resultado_teste.append(f"ID {idFone} - Preço: {'PASS' if preco_check else 'FAIL'}")
        resultado_teste.append(f"ID {idFone} - Quantidade: {'PASS' if qtd_check else 'FAIL'}")

        assert modelo_check, f"Erro: 'modelo' é NULL para ID {idFone}"
        assert tipo_check, f"Erro: 'tipo' é NULL para ID {idFone}"
        assert marca_check, f"Erro: 'marca' é NULL para ID {idFone}"
        assert preco_check, f"Erro: 'preco' é NULL para ID {idFone}"
        assert qtd_check, f"Erro: 'qtd' é NULL para ID {idFone}"

    # Salva os resultados no arquivo 'test_results.txt'
    with open("test_results.txt", "a") as file:
        for resultado in resultado_teste:
            file.write(resultado + "\n")
