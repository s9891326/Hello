import datetime
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, update, delete

from hello_fastapi.follow_ithelp.sync.api.depends import PaginationParms, pagination_params, verify_token
from hello_fastapi.follow_ithelp.sync.database.fake_db import get_db
from hello_fastapi.follow_ithelp.sync.database.generic import get_db2
from hello_fastapi.follow_ithelp.models.item import Item
from hello_fastapi.follow_ithelp.models.users import User
from hello_fastapi.follow_ithelp.schemas import users as UserSchema
from hello_fastapi.follow_ithelp.sync.crud import users as UserCrud
from starlette import status

router = APIRouter(
    tags=["users"],
    prefix="/api",
    # dependencies=[Depends(verify_token)]
)
fake_db = get_db()
db_session = get_db2()


# @router.get("/users")
# async def read_users():
#     return [{"username": "Foo"}, {"username": "Bar"}]
#
#
# @router.get("/users", response_model=list[UserSchema.UserRead])
# def get_users():
#     return fake_db["users"]


# @router.get("/users/{user_id}", response_model=UserSchema.UserRead)
# def get_user(user_id: int):
#     """
#     Create an user list with all the information:2
#
#     - **id**
#     - **name**
#     - **email**
#     - **avatar**
#
#     """
#     for user in fake_db["users"]:
#         if isinstance(user, UserSchema.UserCreate):
#             _user_id = user.id
#         else:
#             _user_id = user["id"]
#
#         if user_id == _user_id:
#             return user
#     raise HTTPException(status_code=404, detail="User not found")


# @router.post(
#     "/users",
#     response_model=UserSchema.UserCreateResponse,
#     response_description="Create user",
#     status_code=status.HTTP_201_CREATED,
# )
# def create_users(user: UserSchema.UserCreate):
#     fake_db["users"].append(user)
#     return user


# @router.delete("/users/{user_id}")
# def delete_users(user_id: int):
#     for user in fake_db["users"]:
#         if user["id"] == user_id:
#             fake_db["users"].remove(user)
#             return user
#
#     return {"error": "User not found"}


@router.get("/test/create")
def create_test():
    result = {
        "user": None,
        "item": None,
    }
    try:
        test_user = User(
            "123456", "test0", 0, None, datetime.datetime(2023, 11, 11), "123@email.com"
        )
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


@router.post(
    "/users",
    response_model=UserSchema.UserCreateResponse,
    response_description="Create user",
    status_code=status.HTTP_201_CREATED,
)
def create_users(new_user: UserSchema.UserCreate):
    user = UserCrud.get_user_id_by_email(new_user.email)
    if user:
        raise HTTPException(status_code=409, detail="User already exists")

    user = UserCrud.create_user(new_user)
    return user


@router.get("/users/{user_id}", response_model=UserSchema.UserRead)
def get_user_by_id(user_id: int):
    stmt = select(User.name, User.id, User.email, User.avatar).where(User.id == user_id)
    user = db_session.execute(stmt).first()
    if user:
        return user

    raise HTTPException(status_code=404, detail="User not found")


@router.get(
    "/users",
    response_model=List[UserSchema.UserRead],
    response_description="Get list of user",
)
def get_users(page_params=Depends(pagination_params)):
    # stmt = select(User.name, User.id, User.email, User.avatar)
    # users = db_session.execute(stmt).all()
    # return users
    return UserCrud.get_users(**page_params)


def check_user_id(user_id):
    stmt = select(User.id).where(User.id == user_id)
    user = db_session.execute(stmt).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.id


@router.patch("/users/{user_id}", response_model=UserSchema.UserUpdateResponse)
def update_users(
    new_user: UserSchema.UserUpdate, user_id: int = Depends(check_user_id)
):
    update_column = {key: value for key, value in new_user if value}
    stmt = update(User).where(User.id == user_id).values(update_column)
    db_session.execute(stmt)
    db_session.commit()

    stmt = select(User.id, User.name, User.avatar, User.age, User.birthday).where(
        User.id == user_id
    )
    user = db_session.execute(stmt).first()

    return user


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_users(user_id: int = Depends(check_user_id)):
    stmt = delete(User).where(User.id == user_id)
    db_session.execute(stmt)
    db_session.commit()
    return
