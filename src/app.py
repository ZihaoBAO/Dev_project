from fastapi import FastAPI
import joblib
import pandas as pd
from sklearn.datasets import load_digits

app = FastAPI()

# Chargement du modèle
try:
    model = joblib.load("models/random_forest_model/model.joblib")
    print("✅ Modèle chargé avec succès")
except Exception as e:
    model = None
    print(f"❌ Erreur lors du chargement du modèle : {e}")

# Route de test
@app.get("/")
def root():
    return {"message": "API UP ✅"}

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
