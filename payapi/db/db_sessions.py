from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)
from config import settings
import asyncio


class DBSessionManager:
    def __init__(
        self, db_url: str = settings.DATABASE_URL, echo: bool = settings.DEBUG
    ):
        self.db_url = db_url
        self.echo = echo
        self.async_engine = create_async_engine(self.db_url, echo=self.echo)
        self.session_factory = async_sessionmaker(
            self.async_engine, expire_on_commit=False
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            self.session_factory, scopefunc=asyncio.current_task
        )
        return session

    async def scoped_session_dependency(self):
        session = self.get_scoped_session()
        yield session
        await session.close()


db_session_manager = DBSessionManager()
