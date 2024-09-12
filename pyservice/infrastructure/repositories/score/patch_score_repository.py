from sqlalchemy import update
from uuid import UUID
from pyservice.infrastructure.models.score_model import ScoreModel
from sqlalchemy.orm import Session
from logging import exception


def patch_score_repository(db, score_id: UUID, name: str, math_score: int, english_score: int):
    with Session(db) as session:
        try:
            row = db.query(ScoreModel).filter(ScoreModel.id == score_id).first()

            if row.name != name:
                query = (update(ScoreModel).where(ScoreModel.id == score_id).values({'name': name}))
                db.execute(query)

            if row.math_score != math_score:
                query = (update(ScoreModel).where(ScoreModel.id == score_id).values({'math_score': math_score}))
                db.execute(query)

            if row.english_score != english_score:
                query = (update(ScoreModel).where(ScoreModel.id == score_id).values({'english_score': english_score}))
                db.execute(query)

            db.commit()
            session.commit()

            return {"Message": "Updated successfully!"}

        except Exception as ex:
            session.rollback()
            # TODO: Log the errors to OpenTelemetry
            exception(f"Error: {ex}")
