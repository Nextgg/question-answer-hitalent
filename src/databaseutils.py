from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
import os

# DATABASE_URL = os.environ.get('DATABASE_URL','postgresql+asyncpg://postgres:password@db:5432/hitalent')
DATABASE_URL = "postgresql+asyncpg://postgres:12qwaszx@localhost:5432/hitalent"

engine = create_async_engine(DATABASE_URL)

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with new_session() as session:
        yield session


class Base(DeclarativeBase):
    pass