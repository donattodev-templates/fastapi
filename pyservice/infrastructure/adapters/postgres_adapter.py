from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO: Implements a interface for the adapter and test with MySQL
# TODO: Move the connection string to a configuration file, check if is possible to re-use pyproject.toml
# TODO: Create a development vs production (for the docker container) connection string

SQLALCHEMY_DATABASE_URL = 'postgresql://d5uRf3S76W98prJF4cCKqw:P2uADnKtBYVkNpjZ68drFS@localhost/pyservice-db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
