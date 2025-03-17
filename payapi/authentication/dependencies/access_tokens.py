from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from db.db_sessions import db_session_manager
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from authentication.models import AccessToken
from typing import Annotated


async def get_access_token_db(
    session: Annotated[
        "AsyncSession", Depends(db_session_manager.scoped_session_dependency)
    ],
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
