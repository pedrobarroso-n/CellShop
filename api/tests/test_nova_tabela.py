import sqlite3
import pytest

@pytest.fixture
def conexao():
    """Cria um banco de dados temporário em memória para testes."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # Criando a nova tabela `pelicula_camera`
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pelicula_camera (
            idPeliculaCam INTEGER PRIMARY KEY AUTOINCREMENT,
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

def test_tabela_pelicula_camera_existe(conexao):
    """Verifica se a tabela 'pelicula_camera' foi criada corretamente e salva o resultado em um arquivo."""
    resultado_teste = []  # Lista para armazenar os resultados do teste
    
    cursor = conexao.cursor()
    
    # Consulta para verificar se a tabela existe no banco de dados
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='pelicula_camera'")
    tabela = cursor.fetchone()
    
    tabela_existe = tabela is not None
    resultado_teste.append(f"Tabela 'pelicula_camera' existe: {'PASS' if tabela_existe else 'FAIL'}")

    # Salva os resultados no arquivo 'test_results.txt'
    with open("test_results.txt", "w") as file:
        for resultado in resultado_teste:
            file.write(resultado + "\n")

    # Asserção para pytest
    assert tabela_existe, "Erro: A tabela 'pelicula_camera' não foi criada!"
