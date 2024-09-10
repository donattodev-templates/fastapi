# from fastapi import APIRouter, HTTPException
#
from pyservice.domain.entities.score import Score
from pyservice.infrastructure.repositories.score.add_score_repository import add_score_repository
# from pyservice.infrastructure.repositories.score.get_score_repository import get_score_repository

from fastapi import APIRouter, HTTPException, Depends
from pyservice.infrastructure.repositories.score.get_score_repository import get_score_repository
from pyservice.infrastructure.adapters.postgres_adapter import get_db
from sqlalchemy.orm import Session
from uuid import UUID

router = APIRouter(
    prefix='/scores',
    tags=['Scores']
)

@router.post("/submit-score")
async def submit_score(score: Score):
    try:
        return add_score_repository(score.id, score.name, score.math_score, score.english_score)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error: {ex}")

# @router.get("/")
# async def submit_score(score: Score):
#     try:
#         return get_score_repository()
#     except Exception as ex:
#         raise HTTPException(status_code=500, detail=f"Error: {ex}")

@router.get("/{score_id}")
async def get_score(score_id: UUID, db: Session = Depends(get_db)):
    try:
        score = get_score_repository(db, score_id)
        if score is None:
            raise HTTPException(status_code=404, detail="Score not found")
        return score
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error: {ex}")