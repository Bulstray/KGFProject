from contextlib import asynccontextmanager

from core.models import Base, db_helper

from fastapi import FastAPI
from typing import AsyncIterator


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield None

    await db_helper.dispose()
