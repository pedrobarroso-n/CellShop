import sqlite3
import pytest

@pytest.fixture
def conexao():
    """Cria um banco de dados temporário em memória para testes."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS capa (
            idCP INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            cor TEXT NOT NULL,
            material TEXT NOT NULL,
            img TEXT,
            preco REAL NOT NULL,
            qtd INTEGER NOT NULL
        )
    """)
    conn.commit()
    yield conn  # Retorna a conexão para ser usada nos testes
    conn.close()

def test_atualizar_quantidade(conexao):
    """Verifica se conseguimos atualizar a quantidade de um item na tabela 'capa'."""
    cursor = conexao.cursor()
    
    # Inserindo um produto na tabela
    cursor.execute("""
        INSERT INTO capa (modelo, cor, material, img, preco, qtd)
        VALUES ('iPhone 13', 'Preto', 'Silicone', 'imagem.jpg', 49.99, 10)
    """)
    conexao.commit()

    # Atualizando a quantidade do produto
    nova_quantidade = 5
    cursor.execute("UPDATE capa SET qtd = ? WHERE modelo = ?", (nova_quantidade, 'iPhone 13'))
    conexao.commit()

    # Recuperando os dados atualizados
    cursor.execute("SELECT qtd FROM capa WHERE modelo = 'iPhone 13'")
    qtd_atualizada = cursor.fetchone()[0]

    # Verificando se a atualização foi bem-sucedida
    assert qtd_atualizada == nova_quantidade, f"Esperado {nova_quantidade}, mas recebeu {qtd_atualizada}"
