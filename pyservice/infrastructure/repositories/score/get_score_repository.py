from uuid import UUID
from sqlalchemy.orm import Session
from pyservice.infrastructure.models.score_model import ScoreModel


def get_score_repository(db: Session, score_id: UUID):
    score = db.query(ScoreModel).filter(ScoreModel.id == score_id).first()

    # TODO: Search for the best way to handle exceptions here

    if score is None:
        return None  # Or raise an exception, depending on your error handling strategy

    return score
