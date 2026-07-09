from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.database import session

app = FastAPI()


@app.get("/")
def read_root():
    result = session.execute(text("SELECT 1")).scalar_one()
    return {"message": "DB connected", "result": result}
