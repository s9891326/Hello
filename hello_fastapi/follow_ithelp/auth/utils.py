from fastapi import Depends, HTTPException, status

from hello_fastapi.follow_ithelp.auth.jwt import verify_access_token
from hello_fastapi.follow_ithelp.crud.users import (
    UserCrudManager,
    get_user_crud_manager,
)
from hello_fastapi.follow_ithelp.schemas.auth import oauth2_token_scheme
from hello_fastapi.follow_ithelp.schemas.users import UserRead

user_crud_manager = Depends(get_user_crud_manager)


async def get_username_id_by_payload(payload) -> (str, str):
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    username: str = payload.get("username")
    u_id: int = payload.get("id")
    if not (username or u_id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token ( No `username` 、 `id` in payload )",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return username, u_id


async def get_current_user(
    token: oauth2_token_scheme,
    user_crud: UserCrudManager = user_crud_manager,
):
    payload: dict = await verify_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    username, _ = await get_username_id_by_payload(payload)
    user: UserRead = await user_crud.get_user_by_username(username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user
