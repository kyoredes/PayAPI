from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from payapi.users.user_manager import UserManager
from typing import Annotated

from fastapi import Depends
from payapi.authentication.dependencies.users import get_user_db


async def get_user_manager(
    users_db: Annotated["SQLAlchemyUserDatabase", Depends(get_user_db)],
):
    yield UserManager(users_db)
