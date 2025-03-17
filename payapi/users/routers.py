from fastapi import APIRouter
from payapi.authentication.dependencies.fastapi_users_router import fastapi_users_router
from payapi.authentication.dependencies.backend import auth_backend
from payapi.users.schemas import UserUpdate, UserRead

users_router = APIRouter(prefix="/users", tags=["users"])

users_router.include_router(
    fastapi_users_router.get_users_router(UserRead, UserUpdate),
)
