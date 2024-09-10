from pyservice.infrastructure.adapters.postgres_adapter import Base
from sqlalchemy import Column, UUID, String, Integer

class ScoreModel(Base):
    __tablename__ = "score"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    math_score = Column(Integer, nullable=False)
    english_score = Column(Integer, nullable=False)
