from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from hello_fastapi.database import Base, Engine


class User(Base):
    # create __tablename__ attribute，宣告 model 對應的 database table name
    __tablename__ = "users"
    # create class attribute，宣告 model 對應的 table field/column
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), index=True)
    fullname = Column(String(50))
    nickname = Column(String(20))
    
    # email = Column(String(50), unique=True)
    # active = Column(Boolean, default=True)
    # create relationship 建立 Table 關聯
    # books = relationship("Books", back_populates="owner")
    
    def __repr__(self):
        return f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>"
    

# class Books(Base):
#     __tablename__ = "books"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(50), index=True)
#     description = Column(String(100))
#     price = Column(Integer)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#     # create relationship
#     owner = relationship("User", back_populates="books")

# 可以自動創建tables
# if __name__ == '__main__':
#     # 建立Schema
#     Base.metadata.create_all(Engine)
