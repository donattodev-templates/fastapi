from uuid import UUID, uuid4

def add_score_repository(id: uuid4, name: str, math_score: int, english_score: int):
    return { "id": id, "name": name, "math_score": math_score, "english_score": english_score }

from pyservice.infrastructure.adapters.postgres_adapter import get_db
# from pyservice.infrastructure.models.score_model import ScoreModel
#
# def add_score_repository(db, name: str, math_score: int, english_score: int):
#     new_score = ScoreModel(
#         id=uuid4(),
#         name=name,
#         math_score=math_score,
#         english_score=english_score
#     )
#
#     db.add(new_score)
#     db.commit()
#     db.refresh(new_score)  # To populate the new_score object with the database-generated ID
#
#     return new_score  # Return the actual database data