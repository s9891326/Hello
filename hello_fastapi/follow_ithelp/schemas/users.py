from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    email: str
    birthday: date


class UserBase(BaseModel):
    id: int


# class UserCreate(UserBase):
#     password: str
#     name: str
#     avatar: Optional[str] = None
#     age: int
#     email: str
#     birthday: date


class UserCreate(UserBase):
    password: str = Field(emin_length=6)
    name: str = Field(min_length=3)
    avatar: Optional[str] = Field(min_length=3)
    age: int = Field(gt=0, lt=100)
    email: str = Field()
    birthday: date = Field()

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "password": "123456",
                    "name": "user1",
                    "avatar": "https://i.imgur.com/4M34hi2.png",
                    "age": 18,
                    "email": "user1@email.com",
                    "birthday": "2003-01-01"
                }
            ]
        }
    }


class UserRead(UserBase):
    name: str
    email: str
    avatar: Optional[str] = None


class UserCreateResponse(UserBase):
    name: str
    email: str
