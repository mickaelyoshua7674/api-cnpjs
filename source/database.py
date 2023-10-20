from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ

SQLALCHEMY_DATABASE_URL = URL.create(drivername=environ["DB_DRIVERNAME"],
                                     username=environ["DB_USERNAME"],
                                     password=environ["DB_PASSWORD"],
                                     host=environ["DB_HOST"],
                                     port=environ["DB_PORT"],
                                     database=environ["DB_NAME"])

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()