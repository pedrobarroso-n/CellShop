import time
import pytest

def test_home_performance(client):
    """Verifica se a página inicial carrega dentro de um tempo aceitável e salva os resultados em um arquivo."""
    resultado_teste = []  # Lista para armazenar os resultados do teste
    tempo_maximo = 0.5  # Define o tempo máximo permitido (em segundos)
    
    inicio = time.time()  # Marca o tempo inicial
    response = client.get("/")  # Faz uma requisição para a rota "/"
    fim = time.time()  # Marca o tempo final
    
    tempo_resposta = fim - inicio  # Calcula o tempo de resposta
    
    # Verifica se a página respondeu corretamente
    status_code_check = response.status_code == 200
    resultado_teste.append(f"Status Code: {response.status_code} - {'PASS' if status_code_check else 'FAIL'}")

    # Verifica se o tempo de resposta está dentro do limite
    tempo_check = tempo_resposta <= tempo_maximo
    resultado_teste.append(f"Tempo de resposta: {tempo_resposta:.2f}s - {'PASS' if tempo_check else 'FAIL'} (Limite: {tempo_maximo}s)")

    # Salva os resultados no arquivo 'test_results.txt'
    with open("test_results.txt", "w") as file:
        for resultado in resultado_teste:
            file.write(resultado + "\n")

    # Asserções para pytest
    assert status_code_check, "Erro: Página inicial não carregou corretamente!"
    assert tempo_check, f"Erro: Página carregou em {tempo_resposta:.2f}s, acima do limite de {tempo_maximo}s"
