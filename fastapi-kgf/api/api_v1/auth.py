from fastapi import APIRouter

from api.dependencies.auth.backend import auth_backend
from core.config import settings

from .fastapi_users_router import fastapi_users

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

router.include_router(
    router=fastapi_users.get_auth_router(
        auth_backend,
    ),
)
