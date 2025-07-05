from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import joblib
import pandas as pd
from sklearn.datasets import load_digits
import os

app = FastAPI()

# mount static files directory
if os.path.exists("src/static"):
    app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Chargement du modèle
try:
    model = joblib.load("models/random_forest_model/random_forest_model.joblib")
    print("✅ Modèle chargé avec succès")
except Exception as e:
    model = None
    print(f"❌ Erreur lors du chargement du modèle : {e}")

# Route de test
@app.get("/")
def root():
    return {"message": "API UP ✅"}

# Route pour servir la page d'accueil
@app.get("/ui")
def serve_ui():
    return FileResponse("src/static/index.html")

# Route de prédiction
@app.get("/predict")
def predict():
    if model is None:
        return {"error": "Le modèle n'a pas pu être chargé."}

    # Charger les données de test
    digits = load_digits()
    df = pd.DataFrame(digits.data, columns=digits.feature_names)
    df["target"] = digits.target

    # Prédiction sur une ligne aléatoire
    random_line = df.sample(n=1)
    x = random_line.drop(columns=["target"]).to_dict(orient="records")[0]
    y = model.predict(random_line.drop(columns=["target"]).values)

    return {
        "input": x,
        "prediction": float(y[0]),
        "actual": int(random_line["target"].iloc[0])
    }
