import sys
import os
# Ensure the app module is found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

headers = {"X-API-KEY": os.getenv("API_KEY")}

def test_query():
    response = client.post("/query", json={"query": "Show me sales data"}, headers=headers)
    assert response.status_code == 200

def test_explain():
    response = client.post("/explain", json={"query": "Show me sales data"}, headers=headers)
    assert response.status_code == 200

def test_validate():
    response = client.post("/validate", json={"query": "Check sales data"}, headers=headers)
    assert response.status_code == 200
