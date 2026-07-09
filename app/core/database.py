from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DATABASE_URL = "postgresql://postgres:example@localhost:5432/postgres"

engine = create_engine(DATABASE_URL, echo=True)
session = Session(engine)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
