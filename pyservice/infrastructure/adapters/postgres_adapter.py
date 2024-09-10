from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO: Implements a interface for the adapter and test with MySQL

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
