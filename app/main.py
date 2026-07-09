from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import session
from app.routers import api_router

app = FastAPI()
app.include_router(router=api_router)


@app.get("/")
def read_root():
    result = session.execute(text("SELECT 1")).scalar_one()
    return {"message": "DB connected", "result": result}
