from fastapi import APIRouter
from pyservice.domain.entities.score import Score

router = APIRouter()

@router.post("/submit-score")
def submit_score(score: Score):
    print("Received!", score)
    return "Hello, again"
