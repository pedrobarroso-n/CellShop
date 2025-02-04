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
    """Verifica se conseguimos inserir e recuperar um item na tabela 'pelicula'."""
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

    assert pelicula is not None  # Confirma que há um resultado
    assert pelicula[1] == 'Samsung S23'  # Verifica o modelo
    assert pelicula[2] == 'Vidro'  # Verifica o tipo
    assert pelicula[3] == 'imagem.jpg'  # Verifica a imagem
    assert pelicula[4] == 59.99  # Verifica o preço
    assert pelicula[5] == 15  # Verifica a quantidade
