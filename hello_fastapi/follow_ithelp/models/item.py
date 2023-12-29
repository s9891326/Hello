from datetime import date, datetime

from sqlalchemy import ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from hello_fastapi.database import Base
from hello_fastapi.follow_ithelp.models.base import BaseType


class Item(Base):
    __tablename__ = "Item"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column(Float())
    brand: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    create_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    last_login: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    user_id: Mapped[int] = mapped_column(ForeignKey("User.id", ondelete="cascade"))
    user: Mapped["User"] = relationship("User", back_populates="items")

    def __init__(
        self,
        name: str,
        price: float,
        brand: str,
        description: str,
        user_id: int
    ) -> None:
        self.name = name
        self.price = price
        self.brand = brand
        self.description = description
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"<Item(id={self.id}, name={self.name}, price={self.price}, brand={self.brand})>"
