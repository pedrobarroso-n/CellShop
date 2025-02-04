import time
import pytest

def test_home_performance(client):
    """Verifica se a página inicial carrega dentro de um tempo aceitável."""
    tempo_maximo = 0.5  # Define o tempo máximo permitido (em segundos)
    
    inicio = time.time()  # Marca o tempo inicial
    response = client.get("/")  # Faz uma requisição para a rota "/"
    fim = time.time()  # Marca o tempo final
    
    tempo_resposta = fim - inicio  # Calcula o tempo de resposta
    
    assert response.status_code == 200, "Erro: Página inicial não carregou corretamente!"
    assert tempo_resposta <= tempo_maximo, f"Erro: Página carregou em {tempo_resposta:.2f}s, acima do limite de {tempo_maximo}s"
