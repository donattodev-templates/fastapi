from pydantic import BaseModel

class Score(BaseModel):
    name: str
    math_score: int
    english_score: int
