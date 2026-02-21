cat > src/app/main.py << EOF
from fastapi import FastAPI
app = FastAPI(title="Cloud Native Backend API")

@app.get("/")
async def root():
    return {"message": "Azure Cloud-Native Backend Platform"}
EOF

