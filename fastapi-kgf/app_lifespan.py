from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_users.exceptions import UserAlreadyExists

from actions.create_superuser import create_superuser

from core.models import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    try:
        await create_superuser()
    except UserAlreadyExists:
        pass

    yield None

    await db_helper.dispose()
