from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from hello_fastapi.follow_ithelp.models.item import Item
from hello_fastapi.follow_ithelp.models.users import User
from hello_fastapi.follow_ithelp.setting.config import get_settings

settings = get_settings()

# sync
# engine = create_engine(settings.database_url, echo=True, pool_pre_ping=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# async
engine = create_async_engine(settings.database_url, echo=True, pool_pre_ping=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, autocommit=False)

Base = declarative_base()


# def get_db2():
#     return SessionLocal()


@asynccontextmanager
async def get_db2() -> AsyncGenerator:
    async with SessionLocal() as db:
        async with db.begin():
            yield db


# def init_db():
#     Base.metadata.create_all(bind=engine, tables=[User.__table__, Item.__table__])


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_db():
    async with engine.begin() as conn:
        await conn.close()
