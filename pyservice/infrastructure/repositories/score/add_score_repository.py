from uuid import uuid4
from logging import exception
from sqlalchemy.orm import Session
from pyservice.infrastructure.models.score_model import ScoreModel


def add_score_repository(db, name: str, math_score: int, english_score: int):
    with Session(db) as session:
        try:
            row = ScoreModel(
                id=uuid4(),
                name=name,
                math_score=math_score,
                english_score=english_score
            )

            db.add(row)
            db.commit()
            db.refresh(row)

            session.commit()
            return {"Message": "Score created successfully!"}

        except Exception as ex:
            session.rollback()
            # TODO: Log the errors to OpenTelemetry
            exception(f"Error: {ex}")
