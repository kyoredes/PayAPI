from fastapi import FastAPI
from users.routers import auth_users_router

app = FastAPI()

app.include_router(auth_users_router)
