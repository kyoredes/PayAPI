import contextlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
from payapi.db.db_sessions import db_session_manager
from payapi.authentication.dependencies.users import get_user_db
from payapi.users.schemas import UserCreate
from payapi.authentication.dependencies.user_manager import get_user_manager
from payapi.users.user_manager import UserManager
from payapi.users.models import User
import logging
from typing import Annotated
from fastapi import Depends
import asyncio
from payapi.config import superuser_default

get_async_session_context = contextlib.asynccontextmanager(
    db_session_manager.get_scoped_session
)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

email = superuser_default.email
password = superuser_default.password
is_active = superuser_default.is_active
is_superuser = superuser_default.is_superuser
is_verified = superuser_default.is_verified


async def create_user(user_manager: UserManager, user_create: UserCreate) -> User:
    user = await user_manager.create(user_create=user_create, safe=False)
    logging.info("User created")
    return user


async def create_superuser(
    email: str,
    password: str,
    is_active: bool,
    is_superuser: bool,
    is_verified: bool,
    session: Annotated[
        "AsyncSession", Depends(db_session_manager.scoped_session_dependency)
    ],
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    async with get_user_db_context(session) as user_db:
        async with get_user_manager_context(user_db) as user_manager:
            return await create_user(user_manager, user_create)


if __name__ == "__main__":
    asyncio.run(create_superuser())
