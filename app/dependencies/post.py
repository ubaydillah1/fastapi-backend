from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.post import PostRepository
from app.services.post import PostService


def get_post_repository(db: Session = Depends(get_db)) -> PostRepository:
    return PostRepository(db)


def get_post_service(
    repository: PostRepository = Depends(get_post_repository),
) -> PostService:
    return PostService(repository)
