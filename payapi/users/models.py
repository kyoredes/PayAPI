from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from base_models import Base


class User(Base, SQLAlchemyBaseUserTableUUID):
    pass
