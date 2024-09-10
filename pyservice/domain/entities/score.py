from pyservice.domain.entities.base_entity import BaseEntity


class Score(BaseEntity):
    name: str
    math_score: int
    english_score: int

    class Config:
        # orm_mode = True
        from_attributes = True
