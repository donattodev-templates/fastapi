from typing import cast

from sqlalchemy import update
from uuid import uuid4
from pyservice.infrastructure.models.score_model import ScoreModel


def patch_score_repository(db, score_id: uuid4, name: str, math_score: int, english_score: int):

    entry_to_be_updated = db.query(ScoreModel).filter(ScoreModel.id == score_id).first()
    update_data = {}

    if entry_to_be_updated.name != name:
        update_data['name'] = name
    if entry_to_be_updated.math_score != math_score:
        update_data['math_score'] = math_score
    if entry_to_be_updated.english_score != english_score:
        update_data['english_score'] = english_score
    if update_data:
        query = (update(ScoreModel).where(cast("ColumnElement[bool]",entry_to_be_updated.id == score_id))
                                   .values(update_data))
        db.execute(query)
        # TODO: Implements exception and rollback in case of error, apply ACID principles
        db.commit()

    updated_score = db.query(ScoreModel).filter_by(id=id).first()
    return updated_score
