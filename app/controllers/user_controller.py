from uuid import UUID

from app.schemas.user import (
    UserCreate,
    UserDetailResponse,
    UserMessageResponse,
    UserUpdate,
    UsersResponse,
)
from app.services.user import UserService

def list_users(service: UserService) -> UsersResponse | dict:
    return {"message": "Users fetched successfully", "data": service.list_users()}


def get_user(user_id: UUID, service: UserService) -> UserDetailResponse | dict:
    return {"message": "User fetched successfully", "data": service.get_user(user_id)}


def create_user(payload: UserCreate, service: UserService) -> UserDetailResponse | dict:
    return {"message": "User created successfully", "data": service.create_user(payload)}


def update_user(
    user_id: UUID,
    payload: UserUpdate,
    service: UserService,
) -> UserDetailResponse | dict:
    return {
        "message": "User updated successfully",
        "data": service.update_user(user_id, payload),
    }


def delete_user(user_id: UUID, service: UserService) -> UserMessageResponse | dict:
    user = service.get_user(user_id)
    service.delete_user(user_id)
    return {"message": "User deleted successfully", "data": user}
