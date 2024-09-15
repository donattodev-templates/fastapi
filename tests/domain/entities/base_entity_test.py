
from uuid import UUID
from pyservice.domain.entities.base_entity import BaseEntity

def test_base_entity_id_generation():
    entity = BaseEntity()
    assert isinstance(entity.id, UUID)


def test_base_entity_id_uniqueness():
    entity1 = BaseEntity()
    entity2 = BaseEntity()
    assert entity1.id != entity2.id
