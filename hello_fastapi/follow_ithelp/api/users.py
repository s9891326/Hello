import datetime
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from hello_fastapi.follow_ithelp.api.depends import (
    PaginationParms,
    pagination_params,
    verify_token,
)
from hello_fastapi.follow_ithelp.auth.jwt import verify_access_token
from hello_fastapi.follow_ithelp.auth.utils import get_current_user
from hello_fastapi.follow_ithelp.crud.users import (
    get_user_crud_manager,
    UserCrudManager,
)
from hello_fastapi.follow_ithelp.database.fake_db import get_db
from hello_fastapi.follow_ithelp.database.generic import get_db2
from hello_fastapi.follow_ithelp.models.item import Item
from hello_fastapi.follow_ithelp.models.users import User
from hello_fastapi.follow_ithelp.schemas import users as UserSchema
from hello_fastapi.follow_ithelp.crud import users as UserCrud
from starlette import status

from hello_fastapi.follow_ithelp.schemas.auth import oauth2_token_scheme
from hello_fastapi.follow_ithelp.schemas.users import UserRead

router = APIRouter(
    tags=["users"],
    prefix="/api",
    # dependencies=[Depends(verify_token)]
)
fake_db = get_db()
db_depends = Depends(get_db2)
user_crud_manager = Depends(get_user_crud_manager)


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
def create_test(db_session: AsyncSession = db_depends):
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
async def create_users(
    new_user: UserSchema.UserCreate, user_crud: UserCrudManager = user_crud_manager
):
    user = await user_crud.get_user_id_by_email(new_user.email)
    if user:
        raise HTTPException(status_code=409, detail="User already exists")

    user = await user_crud.create_user(new_user)
    return user


@router.get("/users/{user_id}", response_model=UserSchema.UserRead)
async def get_user_by_id(user_id: int, user_crud: UserCrudManager = user_crud_manager):
    user = await user_crud.get_user_by_id(user_id)
    if user:
        return user

    raise HTTPException(status_code=404, detail="User not found")


@router.get(
    "/users",
    response_model=List[UserSchema.UserRead],
    response_description="Get list of user",
)
async def get_users(
    page_params=Depends(pagination_params),
    user_crud: UserCrudManager = user_crud_manager,
):
    # stmt = select(User.name, User.id, User.email, User.avatar)
    # users = db_session.execute(stmt).all()
    # return users
    return await user_crud.get_users(**page_params)


async def check_user_id(user_id, db_session: AsyncSession = db_depends):
    stmt = select(User.id).where(User.id == user_id)
    result = await db_session.execute(stmt)
    user = result.first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.id


@router.patch("/users/{user_id}", response_model=UserSchema.UserUpdateResponse)
async def update_users(
    user_id: str,
    new_user: UserSchema.UserUpdate,
    user_crud: UserCrudManager = user_crud_manager,
    current_user: UserRead = Depends(get_current_user),
):
    if current_user.id != int(user_id):
        raise HTTPException(status_code=403, detail="Permission denied")

    user_id: str = await user_crud.check_user_id(user_id)
    if not user_id:
        raise HTTPException(status_code=404, detail="User not found")

    update_column = {key: value for key, value in new_user if value}
    return await user_crud.update_user(user_id, update_column)


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_users(
    user_id: int = Depends(check_user_id),
    db_session: AsyncSession = db_depends,
    current_user: UserRead = Depends(get_current_user),
):
    if current_user.id != int(user_id):
        raise HTTPException(status_code=403, detail="Permission denied")

    stmt = delete(User).where(User.id == user_id)
    await db_session.execute(stmt)
    await db_session.commit()
    return
