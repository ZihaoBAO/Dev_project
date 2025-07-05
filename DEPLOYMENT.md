# Project Deployment Guide

### 🔄 Steps to Complete

## 1. Branch Management Setup

```bash
# Create development branch
git checkout -b dev
git push -u origin dev

# Create staging branch
git checkout -b staging
git push -u origin staging

# Return to main branch
git checkout main
```

## 2. Configure GitHub Secrets

Add the following secrets in your GitHub repository settings:

- `DOCKERHUB_USER`: Your DockerHub username
- `DOCKERHUB_TOKEN`: Your DockerHub access token

## 3. Test Local Run

```bash
# Install dependencies
pip install -r requirements.txt

# Start application
uvicorn src.app:app --host 0.0.0.0 --port 8000

# Run tests
pytest tests/

# Access frontend interface
# http://localhost:8000/ui
```

## 4. Deploy to Cloud Platform

### Koyeb (Recommended)

1. Visit [koyeb.com](https://koyeb.com)
2. Register and login
3. Click "Create App"
4. Select "Docker" deployment method
5. Enter Docker image: `zihaobao/dev_project:latest`
6. Set port: `8000`
7. Click "Deploy"

## 5. Update End-to-End Tests

After deployment, update the URL in `tests/test_e2e.py`:

```python
BASE_URL = "https://subtle-gabriellia-zihaobao-95b9bb8c.koyeb.app"
```

## 6. Verify Deployment

1. Visit the deployed URL
2. Test `/` endpoint
3. Test `/ui` frontend interface
4. Test `/predict` prediction functionality
5. Run end-to-end tests

## Project URLs

After deployment, add your application URLs here:

**Application URL**: `https://subtle-gabriellia-zihaobao-95b9bb8c.koyeb.app`

**Frontend Interface**: `https://subtle-gabriellia-zihaobao-95b9bb8c.koyeb.app/ui`

**API Documentation**: `https://subtle-gabriellia-zihaobao-95b9bb8c.koyeb.app/docs` 

**Prediction Function**: `https://subtle-gabriellia-zihaobao-95b9bb8c.koyeb.app/predict`