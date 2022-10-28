from typing import List

from pydantic import BaseModel, Field


class Books(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    price: int = Field(...)
    owner_id: int = Field(...)


class UserBase(BaseModel):
    name: str
    fullname: str
    nickname: str


class UserUpdate(UserBase):
    id: int
    
    class Config:
        orm_mode = True


class UserType(BaseModel):
    skip: int
    limit: int
    data: List[UserUpdate]
