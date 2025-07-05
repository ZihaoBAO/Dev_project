from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app


client = TestClient(app)

def test_root_endpoint():
    """test if the root endpoint is working"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "API UP ✅"

def test_predict_endpoint():
    """test if the predict endpoint is working"""
    response = client.get("/predict")
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "input" in data
    assert "actual" in data
    assert isinstance(data["prediction"], float)
    assert isinstance(data["actual"], int)

def test_predict_response_structure():
    """test if the predict response structure is correct"""
    response = client.get("/predict")
    data = response.json()
    
    # test if the input data format is correct
    assert isinstance(data["input"], dict)
    assert len(data["input"]) > 0
    
    # test if the prediction value range is correct (0-9, because it's a digit recognition)
    assert 0 <= data["prediction"] <= 9
    assert 0 <= data["actual"] <= 9
