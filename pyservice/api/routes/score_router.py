from uuid import UUID
from sqlalchemy.orm import Session
from pyservice.domain.entities.score import Score
from fastapi import APIRouter, HTTPException, Depends
from pyservice.infrastructure.adapters.databases.postgres_adapter import get_db
from pyservice.infrastructure.repositories.score.add_score_repository import add_score_repository
from pyservice.infrastructure.repositories.score.delete_score_repository import delete_score_repository
from pyservice.infrastructure.repositories.score.get_all_score_repository import get_all_score_repository
from pyservice.infrastructure.repositories.score.get_score_repository import get_score_repository
from pyservice.infrastructure.repositories.score.patch_score_repository import patch_score_repository
from pyservice.infrastructure.repositories.score.put_score_repository import put_score_repository


router = APIRouter(
    prefix='/scores',
    tags=['Scores']
)


@router.get("/")
async def get_all_scores(db: Session = Depends(get_db)):
    try:
        return get_all_score_repository(db)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error: {ex}")


@router.get("/{score_id}")
async def get_score(score_id: UUID, db: Session = Depends(get_db)):
    try:
        score = get_score_repository(db, score_id)
        if score is None:
            raise HTTPException(status_code=404, detail="Score not found")
        return score
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error: {ex}")


@router.post("/submit-score")
async def post_score(score: Score, db: Session = Depends(get_db)):
    try:
        return add_score_repository(db, score.name, score.math_score, score.english_score)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error: {ex}")


@router.put("/replace-score/{score_id}")
async def put_score(score_id: UUID, score: Score, db: Session = Depends(get_db)):
    try:
        return put_score_repository(db, score_id, score.name, score.math_score, score.english_score)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error: {ex}")


@router.patch("/update-score/{score_id}")
async def patch_score(score_id: UUID, score: Score, db: Session = Depends(get_db)):
    try:
        return patch_score_repository(db, score_id, score.name, score.math_score, score.english_score)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error: {ex}")


@router.delete("/delete-score/{score_id}")
async def patch_score(score_id: UUID, db: Session = Depends(get_db)):
    try:
        return delete_score_repository(db, score_id)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error: {ex}")
