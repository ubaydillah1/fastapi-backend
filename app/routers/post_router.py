from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.controllers.post_controller import (
    create_post,
    delete_post,
    get_post,
    list_posts,
    update_post,
)
from app.dependencies.post import get_post_service
from app.schemas.post import (
    CreatePost,
    PostDetailResponse,
    PostMessageResponse,
    PostsResponse,
    UpdatePost,
)
from app.services.post import PostService

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("", response_model=PostsResponse)
def list_post_route(service: PostService = Depends(get_post_service)):
    return list_posts(service)


@router.get("/{post_id}", response_model=PostDetailResponse)
def get_post_route(post_id: UUID, service: PostService = Depends(get_post_service)):
    return get_post(post_id, service)


@router.post(
    "",
    response_model=PostDetailResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_post_route(
    payload: CreatePost,
    service: PostService = Depends(get_post_service),
):
    return create_post(payload, service)


@router.put("/{post_id}", response_model=PostDetailResponse)
def update_post_route(
    post_id: UUID,
    payload: UpdatePost,
    service: PostService = Depends(get_post_service),
):
    return update_post(post_id, payload, service)


@router.delete("/{post_id}", response_model=PostMessageResponse)
def delete_post_route(post_id: UUID, service: PostService = Depends(get_post_service)):
    return delete_post(post_id, service)
