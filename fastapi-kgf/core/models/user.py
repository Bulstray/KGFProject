from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from core.types import UserIdType

from .base import Base
from .mixin import IdIntPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from .access_token import AccessToken


class User(SQLAlchemyBaseUserTable[UserIdType], IdIntPkMixin, Base):

    name: Mapped[str] = mapped_column(String(50))

    surname: Mapped[str] = mapped_column(String(50))

    @classmethod
    def get_db(cls, session: "AsyncSession") -> SQLAlchemyUserDatabase:
        return SQLAlchemyUserDatabase(session, cls)
