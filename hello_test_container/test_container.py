import unittest
from functools import wraps

import warnings
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from testcontainers.postgres import PostgresContainer

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    uid = Column(String(100), primary_key=True, unique=True, index=True)
    name = Column(String(100))
    age = Column(Integer)

    def __str__(self):
        return f"User uid: {self.uid}, name: {self.name}, age: {self.age}"


def create_user(db, user):
    db_user = User(uid=user.uid, name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    return db_user


def db_mask(func):
    @wraps(func)
    def wrapper(*args):
        with PostgresContainer("postgres:9.5") as postgres:
            engine = sqlalchemy.create_engine(postgres.get_connection_url())
            session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            Base.metadata.create_all(bind=engine)

            db = session_local()
            try:
                func(db=db, *args)
            finally:
                print("close db")
                db.close()
    return wrapper


class TestUserCRUD(unittest.TestCase):
    def setUp(self) -> None:
        # 解决ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)

    @db_mask
    def test_create_user(self, db):
        user = create_user(db, User(uid="1", name="eddy", age=18))

        self.assertEqual(user.uid, "1")
        self.assertEqual(user.name, "eddy")
        self.assertEqual(user.age, 18)
        print(user)


if __name__ == '__main__':
    unittest.main()
