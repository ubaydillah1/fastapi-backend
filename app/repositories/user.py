from uuid import UUID

from sqlalchemy.orm import Session

from app.models.table import User
from app.schemas.user import UserCreate, UserUpdate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[User]:
        return self.db.query(User).all()

    def get_by_id(self, user_id: UUID) -> User | None:
        return self.db.get(User, user_id)

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def create(self, payload: UserCreate) -> User:
        user = User(
            name=payload.name,
            age=payload.age,
            email=payload.email,
            password=payload.password,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def create_auth_user(
        self,
        *,
        email: str,
        password: str,
        name: str,
        age: int,
    ) -> User:
        user = User(email=email, password=password, name=name, age=age)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, user: User, payload: UserUpdate) -> User:
        updates = payload.model_dump(exclude_unset=True)
        for field, value in updates.items():
            setattr(user, field, value)

        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()
