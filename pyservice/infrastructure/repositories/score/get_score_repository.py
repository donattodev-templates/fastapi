from uuid import UUID
from logging import exception
from sqlalchemy.orm import Session
from pyservice.infrastructure.models.score_model import ScoreModel


def get_score_repository(db: Session, score_id: UUID):
    try:
        score = db.query(ScoreModel).filter(ScoreModel.id == score_id).first()
        return score

    except Exception as ex:
        # TODO: Log the errors to OpenTelemetry
        exception(f"Error: {ex}")
