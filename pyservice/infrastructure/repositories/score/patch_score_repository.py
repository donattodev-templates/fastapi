from sqlalchemy import update
from uuid import UUID
from pyservice.infrastructure.models.score_model import ScoreModel
from sqlalchemy.orm import Session


def patch_score_repository(db, score_id: UUID, name: str, math_score: int, english_score: int):
    with Session(db) as session:
        try:
            row = db.query(ScoreModel).filter(ScoreModel.id == score_id).first()

            if row.name != name:
                query = (update(ScoreModel).where(ScoreModel.id == score_id).values({'name': name}))

            if row.math_score != math_score:
                query = (update(ScoreModel).where(ScoreModel.id == score_id).values({'math_score': math_score}))

            if row.english_score != english_score:
                query = (update(ScoreModel).where(ScoreModel.id == score_id).values({'english_score': english_score}))

            db.execute(query)
            db.commit()
            session.commit()

            return {"Message": "Updated successfully!"}

        except Exception:
            session.rollback()
            # TODO: Handle the exception appropriately (log, return error message, etc.)
            raise  # Re-raise the exception for now
