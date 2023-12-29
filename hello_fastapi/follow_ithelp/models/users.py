import hashlib
from datetime import date, datetime
from typing import Optional

from sqlalchemy import Date, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from hello_fastapi.database import Base
from hello_fastapi.follow_ithelp.models.base import BaseType


# class User(Base):
#     __tablename__ = "User"
#     id: Mapped[BaseType.int_primary_key]
#     password: Mapped[BaseType.str_50]
#     name: Mapped[BaseType.str_30]
#     age: Mapped[int]
#     avatar: Mapped[BaseType.optional_str_100]
#     birthday: Mapped[date] = mapped_column(Date)
#     email: Mapped[BaseType.str_50]
#     create_time: Mapped[BaseType.update_time]
#
#     items: Mapped[list["Item"]] = relationship(
#         "Item",
#         back_populates="user",
#         cascade="all, delete-orphan",
#         lazy="select",
#         order_by="Item.name",
#     )
#
#     def __init__(
#         self,
#         password: str,
#         name: str,
#         age: int,
#         avatar: Optional[str],
#         birthday: date,
#         email: str,
#     ) -> None:
#         # password should be hashed before store in database , here is just for demo
#         self.password = hashlib.md5(password.encode() + b"secret").hexdigest()
#         self.name = name
#         self.age = age
#         self.avatar = avatar
#         self.birthday = birthday
#         self.email = email
#
#     def __repr__(self) -> str:
#         return f"<User(id={self.id}, name={self.name}, age={self.age}, email={self.email})>"


class User(Base):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
    password: Mapped[str] = mapped_column(String(50))
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int]
    avatar: Mapped[str] = mapped_column(String(100), nullable=True)
    birthday: Mapped[date] = mapped_column(Date)
    email: Mapped[str] = mapped_column(String(50))
    create_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    items: Mapped[list["Item"]] = relationship(
        "Item",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="select",
        order_by="Item.name",
    )

    def __init__(
        self,
        password: str,
        name: str,
        age: int,
        avatar: Optional[str],
        birthday: date,
        email: str,
    ) -> None:
        # password should be hashed before store in database , here is just for demo
        self.password = hashlib.md5(password.encode() + b"secret").hexdigest()
        self.name = name
        self.age = age
        self.avatar = avatar
        self.birthday = birthday
        self.email = email

    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name}, age={self.age}, email={self.email})>"
