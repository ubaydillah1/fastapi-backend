from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CreatePost(BaseModel):
    name: str
    description: str
    user_id: UUID


class UpdatePost(BaseModel):
    name: str | None = None
    description: str | None = None
    user_id: UUID | None = None


class PostResponse(BaseModel):
    id: UUID
    name: str
    description: str
    user_id: UUID
    model_config = ConfigDict(from_attributes=True)


class PostDetailResponse(BaseModel):
    message: str
    data: PostResponse


class PostsResponse(BaseModel):
    message: str
    data: list[PostResponse]


class PostMessageResponse(BaseModel):
    message: str
    data: PostResponse | None
