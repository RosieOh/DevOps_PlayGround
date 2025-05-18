from fastapi import APIRouter

from app.models import Model

router = APIRouter()
models = {}

@router.get("/metrics")
async def get_metrics():
    metrics = {}
    for model_id, model in models.items():
        metrics[model_id] = model.metadata
    return metrics