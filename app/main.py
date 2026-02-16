# app/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import init_db
from app.model_controller import router as model_router
from app.monitor import router as monitor_router
from app.version_controller import router as version_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(model_router, prefix="/models")
app.include_router(version_router, prefix="/models")
app.include_router(monitor_router, prefix="/monitor")

@app.get("/")
async def root():
    return {"message": "Welcome to MCP Server!"}