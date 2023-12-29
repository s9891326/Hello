import datetime

from fastapi import APIRouter, HTTPException
from hello_fastapi.follow_ithelp.database.fake_db import get_db
from hello_fastapi.follow_ithelp.database.generic import get_db2
from hello_fastapi.follow_ithelp.models.item import Item
from hello_fastapi.follow_ithelp.models.users import User
from hello_fastapi.follow_ithelp.schemas import users as UserSchema
from starlette import status

router = APIRouter(tags=["users"], prefix="/api")
fake_db = get_db()


@router.get("/users")
async def read_users():
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.get("/users", response_model=list[UserSchema.UserRead])
def get_users():
    return fake_db["users"]


@router.get("/users/{user_id}", response_model=UserSchema.UserRead)
def get_user(user_id: int):
    """
    Create an user list with all the information:2

    - **id**
    - **name**
    - **email**
    - **avatar**

    """
    for user in fake_db["users"]:
        if isinstance(user, UserSchema.UserCreate):
            _user_id = user.id
        else:
            _user_id = user["id"]

        if user_id == _user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.post(
    "/users",
    response_model=UserSchema.UserCreateResponse,
    response_description="Create user",
    status_code=status.HTTP_201_CREATED,
)
def create_users(user: UserSchema.UserCreate):
    fake_db["users"].append(user)
    return user


@router.delete("/users/{user_id}")
def delete_users(user_id: int):
    for user in fake_db["users"]:
        if user["id"] == user_id:
            fake_db["users"].remove(user)
            return user

    return {"error": "User not found"}


@router.get("/test/create")
def test():
    db_session = get_db2()
    result = {
        "user": None,
        "item": None,
    }
    try:
        test_user = User("123456", "test0", 0, None, datetime.datetime(2023, 11, 11), "123@email.com")
        db_session.add(test_user)
        db_session.commit()
        result["user"] = test_user

        test_item = Item("item0", 99.9, "brand0", "test0", test_user.id)
        db_session.add(test_item)
        db_session.commit()
        result["user"] = test_user
        result["item"] = test_item

    except Exception as e:
        print(e)

    return result
