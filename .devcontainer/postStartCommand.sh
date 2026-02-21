#!/bin/bash
echo "🚀 Starting Cloud-Native Backend API..."
source .venv/bin/activate || (python3 -m venv .venv && source .venv/bin/activate)
uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload
