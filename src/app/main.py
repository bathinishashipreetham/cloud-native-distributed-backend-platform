cat > src/app/main.py << 'EOF'
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os

app = FastAPI(
    title="Cloud Native Distributed Backend Platform",
    description="Microsoft Azure production backend API",
    version="1.0.0"
)

class HealthResponse(BaseModel):
    status: str = "healthy"
    azure_env: str = os.getenv("AZURE_ENV", "local")

@app.get("/")
async def root():
    return {"message": "Azure Cloud-Native Backend Platform 🚀"}

@app.get("/health")
async def health_check():
    return HealthResponse()

@app.get("/api/v1/services")
async def get_services():
    return [{"service": "distributed-backend", "status": "active", "azure": True}]
EOF
