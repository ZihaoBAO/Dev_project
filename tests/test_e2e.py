import requests

def test_predict_online():
    url = "https://<TON-APP>.railway.app/predict"  # 🔁 remplace ici par l’URL réelle
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
