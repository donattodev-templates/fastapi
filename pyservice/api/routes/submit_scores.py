from fastapi import APIRouter, HTTPException

from pyservice.domain.entities.score import Score
from pyservice.infrastructure.repositories.add_score_repository import add_score_repository

router = APIRouter()

@router.post("/submit-score")
async def submit_score(score: Score):
    try:
        return add_score_repository(score.name, score.math_score, score.english_score)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error: {ex}")
