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
    """Verifica se conseguimos atualizar a quantidade de um item na tabela 'capa' e salva os resultados em um arquivo."""
    resultado_teste = []  # Lista para armazenar os resultados do teste
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

    # Verificações
    qtd_check = qtd_atualizada == nova_quantidade

    resultado_teste.append(f"Atualização de quantidade: {'PASS' if qtd_check else 'FAIL'} (Esperado: {nova_quantidade}, Recebido: {qtd_atualizada})")

    # Salva os resultados no arquivo 'test_results.txt'
    with open("test_results.txt", "a") as file:
        for resultado in resultado_teste:
            file.write(resultado + "\n")

    # Asserção para pytest
    assert qtd_check, f"Erro: Esperado {nova_quantidade}, mas recebeu {qtd_atualizada}"
