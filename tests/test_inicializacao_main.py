import pytest
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    resultado_teste = []  # Lista para armazenar os resultados do teste
    
    response = client.get("/")
    
    # Verifica se a página carregou corretamente
    status_code_check = response.status_code == 200
    resultado_teste.append(f"Status Code: {response.status_code} - {'PASS' if status_code_check else 'FAIL'}")

    # Verifica se "CellShop" está na página HTML
    content_check = b"CellShop" in response.data
    resultado_teste.append(f"Texto 'CellShop' encontrado: {'PASS' if content_check else 'FAIL'}")

    # Salva os resultados no arquivo 'test_results.txt'
    with open("test_results.txt", "w") as file:
        for resultado in resultado_teste:
            file.write(resultado + "\n")

    # Asserções para pytest
    assert status_code_check, "Erro: Página não carregou corretamente"
    assert content_check, "Erro: Texto 'CellShop' não encontrado na página"
