# Cloud-Native Distributed Backend Platform ✨

Production-grade **FastAPI backend** deployed on **Microsoft Azure**.

## 🏗️ Architecture

[200~src/app/ # FastAPI application
infra/bicep/ # Azure Bicep IaC
tests/ # pytest suite
azure-pipelines/ # Azure DevOps CI/CD~

## 🚀 Quick Start
```bash
pip install -r requirements-azure.txt
uvicorn src.app.main:app --reload --port 8000

Live API: http://localhost:8000/health
