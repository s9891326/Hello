from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from hello_fastapi.follow_ithelp.models.item import Item
from hello_fastapi.follow_ithelp.models.users import User
from hello_fastapi.follow_ithelp.setting.config import get_settings

settings = get_settings()

engine = create_engine(settings.database_url, echo=True, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db2():
    return SessionLocal()


def init_db():
    Base.metadata.create_all(bind=engine, tables=[User.__table__, Item.__table__])
