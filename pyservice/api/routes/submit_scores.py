from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Score(BaseModel):
    name: str
    math_score: int
    english_score: int

@router.post("/submit-score")
def submit_score(score: Score):
    print("Received!", score)
    return "Hello, again"
