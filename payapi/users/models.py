from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from payapi.base_models import Base


class User(Base, SQLAlchemyBaseUserTableUUID):
    pass
