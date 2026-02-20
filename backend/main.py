"""
NEXUS OS Backend - FastAPI
Sistema de agentes IA para gestión personal y empresarial
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Config
NEXUS_TOKEN = os.getenv("NEXUS_TOKEN", "nexus-secret-2026")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./nexus.db")

# App
app = FastAPI(
    title="NEXUS OS",
    description="Sistema de agentes IA para gestión personal y empresarial",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Auth
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != NEXUS_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )
    return True

# Models
class Agent(BaseModel):
    id: str
    name: str
    role: str
    status: str
    cpu: float
    ram: float
    tasks_today: int
    model: str
    last_seen: Optional[datetime] = None

class Task(BaseModel):
    id: str
    name: str
    status: str
    agent: str
    created_at: datetime

class KPI(BaseModel):
    id: str
    name: str
    value: float
    trend: str
    unit: str

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str

# Mock Data
AGENTS = [
    Agent(id="blackbox", name="BLACKBOX", role="Orquestador/Estrategia", status="online", cpu=12.5, ram=34.2, tasks_today=15, model="qwen2.5-coder"),
    Agent(id="forge", name="FORGE", role="CTO Técnico", status="offline", cpu=0, ram=0, tasks_today=0, model="deepseek-r1"),
    Agent(id="clawmark", name="CLAWMARK", role="Marketing/Growth", status="offline", cpu=0, ram=0, tasks_today=0, model="llama3.1:8b"),
]

TASKS = [
    Task(id="1", name="Configurar OpenClaw", status="done", agent="blackbox", created_at=datetime.now()),
    Task(id="2", name="Fix TalentOs login", status="pending", agent="forge", created_at=datetime.now()),
    Task(id="3", name="Conectar WhatsApp", status="pending", agent="blackbox", created_at=datetime.now()),
]

KPIS = [
    KPI(id="tasks", name="Tareas hoy", value=15, trend="up", unit=""),
    KPI(id="emails", name="Emails procesados", value=42, trend="up", unit=""),
    KPI(id="uptime", name="Uptime", value=99.9, trend="stable", unit="%"),
    KPI(id="cost", name="Coste diario", value=0.00, trend="stable", unit="€"),
]

# Routes
@app.get("/api/health", response_model=HealthResponse)
async def health():
    return HealthResponse(
        status="ok",
        timestamp=datetime.now(),
        version="1.0.0"
    )

@app.get("/api/agents", response_model=List[Agent])
async def get_agents(auth: bool = Depends(verify_token)):
    return AGENTS

@app.get("/api/tasks", response_model=List[Task])
async def get_tasks(auth: bool = Depends(verify_token)):
    return TASKS

@app.get("/api/kpis", response_model=List[KPI])
async def get_kpis(auth: bool = Depends(verify_token)):
    return KPIS

@app.post("/api/tasks")
async def create_task(task: Task, auth: bool = Depends(verify_token)):
    TASKS.append(task)
    return {"status": "created", "task": task}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3334)
