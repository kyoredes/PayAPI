from fastapi import APIRouter
from authentication.dependencies.fastapi_users_router import fastapi_users_router
from authentication.dependencies.backend import auth_backend

auth_users_router = APIRouter(prefix="/auth", tags=["auth"])

auth_users_router.include_router(
    router=fastapi_users_router.get_auth_router(auth_backend)
)
