from dataclasses import dataclass

import psycopg2
import sqlalchemy
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker, declarative_base
from testcontainers.postgres import PostgresContainer

from hello_test_container.crud import create_user

Base = declarative_base()


@dataclass
class UserSchema:
    uid: str
    name: str
    picture: str


def db_mask(postgres):
    engine = sqlalchemy.create_engine(postgres.get_connection_url())
    test_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = test_session_local()
            yield db
        finally:
            db.close()

    return override_get_db()


with PostgresContainer("postgres:9.5") as postgres:
    db = next(db_mask(postgres))
    user = create_user(db, UserSchema(uid="1", name="eddy", picture="https://xx"))
    print(user)

    # engine = sqlalchemy.create_engine(postgres.get_connection_url())
    # test_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # db = test_session_local()
    # rs = db.execute(text("select version()"))
    # for row in rs:
    #     print(row)


