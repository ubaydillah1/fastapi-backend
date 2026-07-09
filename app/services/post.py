from fastapi import HTTPException, status
from app.repositories.post import PostRepository
from app.models.table import Post
from app.schemas.post import UpdatePost, CreatePost
from uuid import UUID


class PostService:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def list_posts(self):
        return self.repository.get_all()

    def get_post(self, post_id: UUID) -> Post:
        post = self.repository.get_by_id(post_id)

        if post is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
            )
        return post

    def create_post(self, payload: CreatePost) -> Post:
        return self.repository.create(payload)

    def update_post(self, post_id: UUID, payload: UpdatePost) -> Post:
        post = self.get_post(post_id)

        return self.repository.update(post, payload)

    def delete_post(self, post_id: UUID) -> None:
        post = self.get_post(post_id)
        self.repository.delete(post)
