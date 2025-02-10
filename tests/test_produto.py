import sqlite3
import pytest

@pytest.fixture
def conexao():
    """Cria um banco de dados temporário em memória para testes."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pelicula (
            idPelicula INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            tipo TEXT NOT NULL,
            img TEXT,
            preco REAL NOT NULL,
            qtd INTEGER NOT NULL
        )
    """)
    conn.commit()
    yield conn  # Retorna a conexão para ser usada nos testes
    conn.close()

def test_inserir_pelicula(conexao):
    """Verifica se conseguimos inserir e recuperar um item na tabela 'pelicula' e salva os resultados em um arquivo."""
    resultado_teste = []  # Lista para armazenar os resultados do teste
    cursor = conexao.cursor()
    
    # Insere um item fictício na tabela
    cursor.execute("""
        INSERT INTO pelicula (modelo, tipo, img, preco, qtd)
        VALUES ('Samsung S23', 'Vidro', 'imagem.jpg', 59.99, 15)
    """)
    conexao.commit()

    # Recupera os dados para ver se foram inseridos corretamente
    cursor.execute("SELECT * FROM pelicula WHERE modelo = 'Samsung S23'")
    pelicula = cursor.fetchone()

    # Verificações
    existencia_check = pelicula is not None
    modelo_check = pelicula[1] == 'Samsung S23'
    tipo_check = pelicula[2] == 'Vidro'
    img_check = pelicula[3] == 'imagem.jpg'
    preco_check = pelicula[4] == 59.99
    qtd_check = pelicula[5] == 15

    resultado_teste.append(f"Item inserido na tabela 'pelicula': {'PASS' if existencia_check else 'FAIL'}")
    resultado_teste.append(f"Modelo correto: {'PASS' if modelo_check else 'FAIL'}")
    resultado_teste.append(f"Tipo correto: {'PASS' if tipo_check else 'FAIL'}")
    resultado_teste.append(f"Imagem correta: {'PASS' if img_check else 'FAIL'}")
    resultado_teste.append(f"Preço correto: {'PASS' if preco_check else 'FAIL'}")
    resultado_teste.append(f"Quantidade correta: {'PASS' if qtd_check else 'FAIL'}")

    # Salva os resultados no arquivo 'test_results.txt'
    with open("test_results.txt", "w") as file:
        for resultado in resultado_teste:
            file.write(resultado + "\n")

    # Asserções para pytest
    assert existencia_check, "Erro: O item não foi inserido na tabela 'pelicula'."
    assert modelo_check, "Erro: O modelo está incorreto."
    assert tipo_check, "Erro: O tipo está incorreto."
    assert img_check, "Erro: A imagem está incorreta."
    assert preco_check, "Erro: O preço está incorreto."
    assert qtd_check, "Erro: A quantidade está incorreta."
