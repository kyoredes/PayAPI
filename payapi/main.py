from fastapi import FastAPI
from payapi.authentication.routers import auth_router
from payapi.users.routers import users_router

app = FastAPI()

# login, logout
app.include_router(auth_router)
app.include_router(users_router)
