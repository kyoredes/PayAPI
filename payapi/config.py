from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    PAYADMIT_TOKEN: str
    PAYADMIT_URL: str
    DEBUG: bool
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str
    SECRET_JWT: str

    class Config:
        env_file = ".env"


class SuperUserDefault(BaseSettings):
    email: str
    password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

    class Config:
        env_file = ".env"
        env_prefix = "superuser_"


settings = Settings()
superuser_default = SuperUserDefault()
