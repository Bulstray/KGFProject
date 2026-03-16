from fastapi_users import schemas
from pydantic import BaseModel

from core.types import UserIdType


class UserBase(BaseModel):
    name: str
    surname: str


class UserRead(schemas.BaseUser[UserIdType], UserBase):
    pass


class UserCreate(schemas.BaseUserCreate, UserBase):
    pass


class UserUpdate(schemas.BaseUserUpdate, UserBase):
    pass
