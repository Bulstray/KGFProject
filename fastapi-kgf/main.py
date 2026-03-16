import uvicorn
from fastapi import FastAPI

from admin import register_admin_views
from api import router
from app_lifespan import lifespan
from core.models import db_helper

from sqladmin import Admin

app = FastAPI(
    lifespan=lifespan,
)

admin = Admin(
    app=app,
    session_maker=db_helper.session_factory,
)

register_admin_views(admin)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app=app)
