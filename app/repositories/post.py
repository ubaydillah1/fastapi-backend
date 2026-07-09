from sqlalchemy.orm import Session
from uuid import UUID

from app.models.table import Post
from app.schemas.post import CreatePost, UpdatePost


class PostRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Post).all()

    def get_by_id(self, post_id: UUID) -> Post | None:
        return self.db.get(Post, post_id)

    def create(self, payload: CreatePost) -> Post:
        post = Post(
            name=payload.name,
            description=payload.description,
            user_id=payload.user_id,
        )

        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)
        return post

    def update(self, post: Post, payload: UpdatePost) -> Post:
        updates = payload.model_dump(exclude_unset=True)

        for field, value in updates.items():
            setattr(post, field, value)

        self.db.commit()
        self.db.refresh(post)

        return post

    def delete(self, post: Post) -> None:
        self.db.delete(post)
        self.db.commit()
