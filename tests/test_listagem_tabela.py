import sqlite3
import pytest

@pytest.fixture
def conexao():
    """Cria um banco de dados temporário em memória para testes."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Criando a tabela 'fone'
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
    
    # Inserindo alguns itens na tabela
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

def test_carregar_todos_itens_fone(client, conexao):
    """Verifica se todos os itens da tabela 'fone' são carregados corretamente na rota /fone."""
    cursor = conexao.cursor()
    
    # Fazendo uma requisição GET para a rota '/fone'
    response = client.get('/fones')
    
    # Verifica se a resposta foi bem-sucedida
    assert response.status_code == 200, "Erro: Página /fone não carregou corretamente!"

    # Recupera todos os itens da tabela 'fone'
    cursor.execute("SELECT * FROM fone")
    itens_fone = cursor.fetchall()

    # Verifica se todos os itens foram carregados na resposta (ou de alguma forma exibidos)
    for item in itens_fone:
        assert item[1] in response.data.decode()  # Verifica se o 'modelo' aparece na resposta
        assert item[2] in response.data.decode()  # Verifica se o 'tipo' aparece na resposta
        assert item[3] in response.data.decode()  # Verifica se a 'marca' aparece na resposta
        assert str(item[4]) in response.data.decode()  # Verifica se a 'img' aparece na resposta
        assert str(item[5]) in response.data.decode()  # Verifica se o 'preco' aparece na resposta
        assert str(item[6]) in response.data.decode()  # Verifica se a 'qtd' aparece na resposta
