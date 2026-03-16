from sqladmin import ModelView
from fastapi import Request, Depends
from api.api_v1.fastapi_users_router import current_active_superuser
from core.models import User


class UserAdmin(ModelView, model=User):
    column_list = [
        User.id,
        User.email,
        # User.hashed_password,
        User.is_active,
        User.is_superuser,
    ]

    column_labels = {
        User.hashed_password: "Password",
    }

    async def is_accessible(self, superuser=Depends(current_active_superuser)):
        print(superuser)
        return True

    can_create = is_accessible
    can_edit = is_accessible
    can_delete = is_accessible
    can_view_details = is_accessible
