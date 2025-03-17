from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi_users.authentication.strategy import AccessTokenDatabase
    from payapi.authentication.models import AccessToken
from fastapi_users.authentication.strategy import DatabaseStrategy
from fastapi import Depends
from payapi.config import settings
from typing import Annotated
from payapi.authentication.dependencies.access_tokens import get_access_token_db


def get_db_strategy(
    access_token_db: Annotated[
        "AccessTokenDatabase[AccessToken]", Depends(get_access_token_db)
    ],
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, settings.lifetime_seconds)
