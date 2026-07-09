from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def list_users(self):
        return self.repository.get_all()

    def get_user(self, user_id: UUID):
        user = self.repository.get_by_id(user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return user

    def create_user(self, payload: UserCreate):
        return self.repository.create(payload)

    def update_user(self, user_id: UUID, payload: UserUpdate):
        user = self.get_user(user_id)
        return self.repository.update(user, payload)

    def delete_user(self, user_id: UUID) -> None:
        user = self.get_user(user_id)
        self.repository.delete(user)
