import requests
import time

# configure test URL (update after deployment)
BASE_URL = "http://localhost:8000"  # local test
# BASE_URL = "https://your-app-url.com"  # production environment test

def test_health_check():
    """end to end test: health check"""
    try:
        response = requests.get(f"{BASE_URL}/", timeout=10)
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "API UP ✅"
        print("✅ health check test passed")
    except requests.exceptions.RequestException as e:
        print(f"❌ health check test failed: {e}")
        assert False

def test_prediction_workflow():
    """end to end test: complete prediction workflow"""
    try:
        # test predict endpoint
        response = requests.get(f"{BASE_URL}/predict", timeout=10)
        assert response.status_code == 200
        
        data = response.json()
        assert "prediction" in data
        assert "input" in data
        assert "actual" in data
        
        # test if the data type is correct
        assert isinstance(data["prediction"], float)
        assert isinstance(data["actual"], int)
        assert isinstance(data["input"], dict)
        
        # test if the prediction value range is correct
        assert 0 <= data["prediction"] <= 9
        assert 0 <= data["actual"] <= 9
        
        print("✅ prediction workflow test passed")
    except requests.exceptions.RequestException as e:
        print(f"❌ prediction workflow test failed: {e}")
        assert False

def test_multiple_predictions():
    """end to end test: multiple predictions consistency"""
    try:
        predictions = []
        for _ in range(3):
            response = requests.get(f"{BASE_URL}/predict", timeout=10)
            assert response.status_code == 200
            data = response.json()
            predictions.append(data["prediction"])
            time.sleep(0.5)  # avoid request too fast
        
        # test if all predictions are in the reasonable range
        for pred in predictions:
            assert 0 <= pred <= 9
        
        print("✅ multiple predictions test passed")
    except requests.exceptions.RequestException as e:
        print(f"❌ multiple predictions test failed: {e}")
        assert False
