from fastapi import APIRouter

from app.routers.post_router import router as post_router
from app.routers.user_router import router as user_router

api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(post_router)
