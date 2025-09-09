import pytest
import sys
from pathlib import Path
from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).parent.parent))

from main import app  


client = TestClient(app)


def test_read_main():
    """Тест для корневого эндпоинта"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


# def test_read_main():
#     """Тест для корневого эндпоинта"""
#     response = client.get("/questions")
#     print(response)
#     assert response.status_code == 200
#     assert response.json() == {}

