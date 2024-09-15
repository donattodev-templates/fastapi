import pytest
from uuid import UUID
from pyservice.domain.entities.score import Score


def test_score_creation():
    score = Score(name="John Doe", math_score=85, english_score=90)
    assert score.name == "John Doe"
    assert score.math_score == 85
    assert score.english_score == 90
    assert isinstance(score.id, UUID)


def test_score_from_dict():
    score_data = {
        "name": "Jane Smith",
        "math_score": 95,
        "english_score": 88
    }
    score = Score(**score_data)
    assert score.name == "Jane Smith"
    assert score.math_score == 95
    assert score.english_score == 88
    assert isinstance(score.id, UUID)


def test_score_validation():
    with pytest.raises(ValueError):
        Score(name="Invalid", math_score="not a number", english_score=80)


def test_score_serialization():
    score = Score(name="Alice", math_score=78, english_score=92)
    serialized = score.model_dump()
    assert serialized["name"] == "Alice"
    assert serialized["math_score"] == 78
    assert serialized["english_score"] == 92
    assert "id" in serialized
