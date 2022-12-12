from sqlalchemy import Column, Integer, String

from hello_postgres_with_sqlalchemy.database import Base, engine


class Test(Base):
    __tablename__ = "test_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(55))
    age = Column(Integer)

    def __str__(self):
        return f"Test<id={self.id}, name={self.name}, age={self.age}>"

    def __repr__(self):
        return f"Test<id={self.id}, name={self.name}, age={self.age}>"


def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    drop_table()
    create_table()
