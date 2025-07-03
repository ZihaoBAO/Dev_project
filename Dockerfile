FROM python:3.12-slim

WORKDIR /app

# Installer git (nécessaire pour DVC)
RUN apt-get update && apt-get install -y git && apt-get clean

# Copier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Installer DVC avec support DagsHub (HTTP)
RUN pip install dvc[http]

# Copier tout le projet
COPY . .

# Récupérer les données suivies par DVC
RUN dvc pull -f || echo "⚠️ DVC pull failed (peut-être en local seulement)"

EXPOSE 8000

# Lancer FastAPI avec support proxy (requis par Koyeb pour le HTTPS)
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--forwarded-allow-ips", "*"]
