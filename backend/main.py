from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from mangum import Mangum
import os
import ai_engine
import database
from models import CodeSnippet

app = FastAPI(title="CodeAssist AI Backend")

# CORS for React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AWS Lambda Handler Wrapper
handler = Mangum(app)

# --- Models ---
class GenerateRequest(BaseModel):
    prompt: str
    language: str = "python"

class DebugRequest(BaseModel):
    code: str
    error_message: Optional[str] = None

class SnippetResponse(BaseModel):
    id: int
    code: str
    description: str

# --- Routes ---

@app.on_event("startup")
def startup():
    database.init_db()

@app.get("/")
def health_check():
    return {"status": "active", "cloud_watch_enabled": True}

@app.post("/generate")
async def generate_code(request: GenerateRequest):
    """Generates optimized code stubs via AI."""
    try:
        result = ai_engine.generate_stub(request.prompt, request.language)
        # Log to DB (Async in real world)
        database.save_log("generation", request.prompt)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/debug")
async def debug_code(request: DebugRequest):
    """Provides debugging insights and fixes."""
    try:
        result = ai_engine.analyze_bug(request.code, request.error_message)
        database.save_log("debugging", request.code[:50])
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history", response_model=List[SnippetResponse])
def get_history():
    """Fetch recent history from PostgreSQL."""
    return database.get_recent_snippets()