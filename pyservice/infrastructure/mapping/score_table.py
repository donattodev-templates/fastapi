from sqlalchemy import Table, Column, Integer, String, MetaData
from pyservice.infrastructure.adapters.postgres_adapter import engine
from sqlalchemy.dialects.postgresql import UUID

def create_score_table():
    """Creates the 'score' table if it doesn't exist."""
    metadata = MetaData()

    Table(
        'score', metadata,
        Column('id', UUID(as_uuid=True), primary_key=True, nullable=False),
        Column('name', String, nullable=False),
        Column('math_score', Integer, nullable=False),
        Column('english_score', Integer, nullable=False)
    )

    metadata.create_all(engine)
