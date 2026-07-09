from uuid import UUID

from app.schemas.post import (
    CreatePost,
    PostDetailResponse,
    PostMessageResponse,
    PostsResponse,
    UpdatePost,
)
from app.services.post import PostService


def list_posts(service: PostService) -> PostsResponse | dict:
    return {"message": "Posts fetched successfully", "data": service.list_posts()}


def get_post(post_id: UUID, service: PostService) -> PostDetailResponse | dict:
    return {"message": "Post fetched successfully", "data": service.get_post(post_id)}


def create_post(payload: CreatePost, service: PostService) -> PostDetailResponse | dict:
    return {
        "message": "Post created successfully",
        "data": service.create_post(payload),
    }


def update_post(
    post_id: UUID,
    payload: UpdatePost,
    service: PostService,
) -> PostDetailResponse | dict:
    return {
        "message": "Post updated successfully",
        "data": service.update_post(post_id, payload),
    }


def delete_post(post_id: UUID, service: PostService) -> PostMessageResponse | dict:
    post = service.get_post(post_id)
    service.delete_post(post_id)
    return {"message": "Post deleted successfully", "data": post}
