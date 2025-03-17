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


settings = Settings()
