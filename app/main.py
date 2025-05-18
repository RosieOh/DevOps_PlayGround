# app/main.py
from fastapi import FastAPI

from app.model_controller import router as model_router
from app.monitor import router as monitor_router
from app.version_controller import router as version_router

app = FastAPI()
app.include_router(model_router, prefix="/models")
app.include_router(version_router, prefix="/models")
app.include_router(monitor_router, prefix="/monitor")

@app.get("/")
async def root():
    return {"message": "Welcome to MCP Server!"}