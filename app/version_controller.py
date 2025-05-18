from fastapi import APIRouter, HTTPException

from app.db import get_model

router = APIRouter()

@router.post("/{model_id}/versions")
async def add_model_version(model_id: str, version: str):
    try:
        model = get_model(model_id)
        model.add_version(version)
        return model.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{model_id}/versions")
async def list_model_versions(model_id: str):
    try:
        model = get_model(model_id)
        return model.versions
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))