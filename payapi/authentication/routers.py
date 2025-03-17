from fastapi import APIRouter
from payapi.authentication.dependencies.fastapi_users_router import fastapi_users_router
from payapi.authentication.dependencies.backend import auth_backend
from payapi.users.schemas import UserCreate, UserRead

auth_router = APIRouter(prefix="/auth", tags=["auth"])

# login, logout
auth_router.include_router(router=fastapi_users_router.get_auth_router(auth_backend))

# register user
auth_router.include_router(
    fastapi_users_router.get_register_router(UserRead, UserCreate),
)
