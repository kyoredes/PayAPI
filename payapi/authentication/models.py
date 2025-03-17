from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTableUUID
from payapi.base_models import Base
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from fastapi_users_db_sqlalchemy.generics import GUID


class AccessToken(Base, SQLAlchemyBaseAccessTokenTableUUID):
    @declared_attr
    def user_id(cls) -> Mapped[GUID]:
        return mapped_column(
            GUID, ForeignKey("users.id", ondelete="cascade"), nullable=False
        )
