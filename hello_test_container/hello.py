import unittest
from dataclasses import dataclass

import psycopg2
import sqlalchemy
from sqlalchemy import text, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from testcontainers.postgres import PostgresContainer

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    uid = Column(String(100), primary_key=True, unique=True, index=True)
    name = Column(String(100))
    picture = Column(String(255))

    def __str__(self):
        return f"User uid: {self.uid}, name: {self.name}, picture: {self.picture}"


def create_user(db: Session, user):
    db_user = User(uid=user.uid, name=user.name, picture=user.picture)
    db.add(db_user)
    db.commit()
    return db_user


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


class TestUserCRUD(unittest.TestCase):
    def test_create_user(self):
        with PostgresContainer("postgres:9.5") as postgres:
            db = next(db_mask(postgres))
            user = create_user(db, UserSchema(uid="1", name="eddy", picture="https://xx"))

            self.assertEqual(user.uid, "1")
            self.assertEqual(user.name, "eddy")
            self.assertEqual(user.picture, "https://xx")
            print(user)
            self.assertEqual(user.uid, "2")


if __name__ == '__main__':
    unittest.main()
