from fastapi import APIRouter, HTTPException, Depends, status

from hello_fastapi.follow_ithelp.auth.jwt import (
    verify_refresh_token,
    create_token_pair,
)
from hello_fastapi.follow_ithelp.auth.utils import (
    get_current_user,
    get_username_id_by_payload,
)
from hello_fastapi.follow_ithelp.crud.users import (
    get_user_crud_manager,
    UserCrudManager,
)
from hello_fastapi.follow_ithelp.schemas.auth import (
    login_form_schema,
    RefreshRequest,
    LoginToken,
)
from hello_fastapi.follow_ithelp.schemas.users import UserRead

router = APIRouter(
    tags=["auth"],
    prefix="/api/auth",
)

user_crud_manager = Depends(get_user_crud_manager)


@router.post("/login", response_model=LoginToken)
async def login(
    form_data: login_form_schema, user_crud: UserCrudManager = user_crud_manager
):
    """
    Login with the following information:

    - **username**
    - **password**

    """
    user: UserRead = await user_crud.get_user_by_username(form_data.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    data = {"username": user.name, "id": user.id}
    return await create_token_pair(data, data)


@router.post("/refresh", response_model=LoginToken)
async def refresh(refresh_data: RefreshRequest):
    """
    Refresh token with the following information:

    - **token** in `Authorization` header

    """
    payload: dict = await verify_refresh_token(refresh_data.refresh_token)
    username, u_id = await get_username_id_by_payload(payload)
    data = {"username": username, "id": u_id}
    return await create_token_pair(data, data)


@router.get("/users/me", response_model=UserRead)
async def read_users_me(current_user: UserRead = Depends(get_current_user)):
    return current_user
