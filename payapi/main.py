from fastapi import FastAPI
from payapi.authentication.routers import auth_router

app = FastAPI()

# login, logout
app.include_router(auth_router)
