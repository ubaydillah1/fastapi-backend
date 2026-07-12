from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    name: str
    age: int


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None


class UserResponse(UserBase):
    id: UUID
    email: str
    model_config = ConfigDict(from_attributes=True)


class UserDetailResponse(BaseModel):
    message: str
    data: UserResponse


class UsersResponse(BaseModel):
    message: str
    data: list[UserResponse]


class UserMessageResponse(BaseModel):
    message: str
    data: UserResponse | None
