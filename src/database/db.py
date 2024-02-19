import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = ("postgresql+psycopg2://postgres:q1234567@localhost:5432"
                           "/contacts")
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# load_dotenv()
#
# SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_URL")
# engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
# AsyncDBSession = async_sessionmaker(
#     bind=engine, expire_on_commit=False, class_=AsyncSession
# )


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
