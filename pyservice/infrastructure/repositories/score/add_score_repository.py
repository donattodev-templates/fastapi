from uuid import uuid4
from pyservice.infrastructure.models.score_model import ScoreModel

def add_score_repository(db, name: str, math_score: int, english_score: int):
    new_score = ScoreModel(
        id=uuid4(),
        name=name,
        math_score=math_score,
        english_score=english_score
    )

    db.add(new_score)
    db.commit()
    db.refresh(new_score)

    return new_score

# Test: curl -X POST "http://127.0.0.1:8000/scores/submit-score" -H "Content-type: application/json" -d '{"name": "John Doe", "math_score": 95, "english_score": 88}'