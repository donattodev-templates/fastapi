from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pyservice.config import get_config

# TODO: Implements a interface for the adapter and test with MySQL

config = get_config()
environment = getenv('ENVIRONMENT', 'development')

if environment == 'production':
    SQLALCHEMY_DATABASE_URL = config['application'] \
                                    ['infrastructure'] \
                                    ['databases'] \
                                    ['postgres'] \
                                    ['connection_strings'] \
                                    ['production']
else:
    SQLALCHEMY_DATABASE_URL = config['application']\
                                    ['infrastructure'] \
                                    ['databases'] \
                                    ['postgres'] \
                                    ['connection_strings'] \
                                    ['development']

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
