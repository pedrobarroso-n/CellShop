import pytest
from main import app  # Importa o app do Flask

@pytest.fixture
def client():
    """Cria um cliente de testes do Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client



