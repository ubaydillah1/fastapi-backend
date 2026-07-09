from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.controllers.user_controller import (
    create_user,
    delete_user,
    get_user,
    list_users,
    update_user,
)
from app.core.database import session
from app.schemas.user import (
    UserCreate,
    UserDetailResponse,
    UserMessageResponse,
    UserUpdate,
    UsersResponse,
)
from app.services.user import UserService

router = APIRouter(prefix="/users", tags=["users"])


def get_user_service() -> UserService:
    return UserService(session)


@router.get("", response_model=UsersResponse)
def list_user_route(service: UserService = Depends(get_user_service)):
    return list_users(service)


@router.get("/{user_id}", response_model=UserDetailResponse)
def get_user_route(user_id: UUID, service: UserService = Depends(get_user_service)):
    return get_user(user_id, service)


@router.post(
    "",
    response_model=UserDetailResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user_route(
    payload: UserCreate,
    service: UserService = Depends(get_user_service),
):
    return create_user(payload, service)


@router.put("/{user_id}", response_model=UserDetailResponse)
def update_user_route(
    user_id: UUID,
    payload: UserUpdate,
    service: UserService = Depends(get_user_service),
):
    return update_user(user_id, payload, service)


@router.delete("/{user_id}", response_model=UserMessageResponse)
def delete_user_route(user_id: UUID, service: UserService = Depends(get_user_service)):
    return delete_user(user_id, service)
