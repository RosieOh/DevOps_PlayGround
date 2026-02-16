from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session

from app.db import ModelMetadata, get_db
from app.models import Model

router = APIRouter()

@router.post("/{model_id}")
async def register_model(
    model_id: str,
    description: str = Form(...),
    db: Session = Depends(get_db)
):
    # 모델 존재 여부 확인
    existing_model = db.query(ModelMetadata).filter(ModelMetadata.model_id == model_id).first()
    if existing_model:
        raise HTTPException(status_code=400, detail="Model already exists")
    
    # 새 모델 생성
    model = ModelMetadata(
        model_id=model_id,
        description=description,
        state="created",
        metadata={
            "request_count": 0,
            "error_count": 0,
            "last_accessed": None
        }
    )
    
    db.add(model)
    db.commit()
    db.refresh(model)
    
    return {
        "model_id": model.model_id,
        "description": model.description,
        "state": model.state,
        "created_at": model.created_at,
        "metadata": model.metadata
    }

@router.put("/{model_id}/state")
async def update_model_state(
    model_id: str,
    state: str,
    db: Session = Depends(get_db)
):
    model = db.query(ModelMetadata).filter(ModelMetadata.model_id == model_id).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    
    # 상태 값 유효성 검사
    valid_states = ["created", "active", "inactive", "archived"]
    if state not in valid_states:
        raise HTTPException(status_code=400, detail=f"Invalid state. Allowed states: {valid_states}")
    
    model.state = state
    db.commit()
    db.refresh(model)
    
    return {
        "model_id": model.model_id,
        "state": model.state,
        "updated_at": model.updated_at
    }

@router.get("/{model_id}/metadata")
async def get_model_metadata(
    model_id: str,
    db: Session = Depends(get_db)
):
    model = db.query(ModelMetadata).filter(ModelMetadata.model_id == model_id).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    
    return model.metadata