from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from config import get_settings

settings = get_settings()

DATABASE_URL = settings.postgres.dsn.unicode_string()

engine = create_async_engine(DATABASE_URL, future=True, echo=True, poolclass=NullPool)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
