from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from typing import List
from src.api.deps import SessionDep
from src.crud.repositories.moveis import movies_repository
from src.crud.schemas.user_schema import UserCreate
from src.crud.models.moveis import MoviesModel
from src.controllers.recommender import generate_recommendations

router = APIRouter()


@router.get("/{usuario_id}/recomendacoes", response_model=List[MoviesModel])
async def get_recommendations(usuario_id: int, session: SessionDep):
    try:
        return generate_recommendations(usuario_id, session)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
