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
    """Verifica se todos os campos NOT NULL da tabela 'fone' têm dados válidos (não nulos)."""
    cursor = conexao.cursor()

    # Recupera todos os itens da tabela 'fone'
    cursor.execute("SELECT * FROM fone")
    itens_fone = cursor.fetchall()

    # Verifica se todos os campos NOT NULL não são NULL
    for item in itens_fone:
        idFone, modelo, tipo, marca, img, preco, qtd = item

        # Verifica se os campos 'modelo', 'tipo', 'marca', 'preco', 'qtd' não são NULL
        assert modelo is not None, "Erro: 'modelo' é NULL"
        assert tipo is not None, "Erro: 'tipo' é NULL"
        assert marca is not None, "Erro: 'marca' é NULL"
        assert preco is not None, "Erro: 'preco' é NULL"
        assert qtd is not None, "Erro: 'qtd' é NULL"

        # O campo 'img' não é NOT NULL, então não precisa ser verificado
        # assert img is not None  # Este campo pode ser NULL, caso necessário, ignore esta verificação
