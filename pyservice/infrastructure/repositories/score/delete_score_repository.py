from logging import exception

from sqlalchemy.orm import Session

from pyservice.infrastructure.models.score_model import ScoreModel
from uuid import UUID

def delete_score_repository(db, score_id: UUID):
    with Session(db) as session:
        try:
            row = db.query(ScoreModel).filter(ScoreModel.id == score_id).first()
            db.delete(row)
            db.commit()

            session.commit()
            return {"Message": "Deleted successfully!"}

        except Exception as ex:
            session.rollback()
            # TODO: Log the errors to OpenTelemetry
            exception(f"Error: {ex}")
