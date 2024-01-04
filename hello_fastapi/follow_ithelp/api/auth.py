from fastapi import APIRouter, HTTPException, Depends

from hello_fastapi.follow_ithelp.auth.jwt import verify_refresh_token, create_token_pair
from hello_fastapi.follow_ithelp.crud.users import (
    get_user_crud_manager,
    UserCrudManager,
)
from hello_fastapi.follow_ithelp.schemas.auth import (
    oauth2_token_scheme,
    login_form_schema,
    RefreshRequest,
    LoginToken,
)
from hello_fastapi.follow_ithelp.schemas.users import UserInDB

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
    user: UserInDB = await user_crud.get_user_by_username(form_data.username)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return await create_token_pair({"username": user.name}, {"username": user.name})
    # return {
    #     "access_token": "login_access_token",
    #     "refresh_token": "login_refresh_token",
    #     "token_type": "bearer",
    # }


@router.post("/refresh", response_model=LoginToken)
async def refresh(refresh_data: RefreshRequest, token: oauth2_token_scheme):
    """
    Refresh token with the following information:

    - **token** in `Authorization` header

    """
    payload: dict = await verify_refresh_token(refresh_data.refresh_token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    username: str = payload.get("username")
    if not username:
        raise HTTPException(
            status_code=401,
            detail="Invalid token ( No `username` in payload )",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return await create_token_pair({"username": username}, {"username": username})
    # return {
    #     "access_token": "new_access_token",
    #     "refresh_token": "new_refresh_token",
    #     "token_type": "bearer",
    # }
