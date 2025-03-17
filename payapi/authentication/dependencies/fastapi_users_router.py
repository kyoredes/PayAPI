from fastapi_users import FastAPIUsers
from users.models import User
import uuid
from authentication.dependencies import user_manager, backend

fastapi_users_router = FastAPIUsers[User, uuid.UUID](
    user_manager.get_user_manager,
    [backend.auth_backend],
)
