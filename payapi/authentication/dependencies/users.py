from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends
from payapi.db.db_sessions import db_session_manager
from fastapi_users.db import SQLAlchemyUserDatabase
from payapi.users.models import User
from typing import Annotated


async def get_user_db(
    session: Annotated[
        "AsyncSession", Depends(db_session_manager.scoped_session_dependency)
    ],
):
    yield SQLAlchemyUserDatabase(session, User)
