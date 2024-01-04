from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

login_form_schema = Annotated[OAuth2PasswordRequestForm, Depends()]
oauth2_token_scheme = Annotated[
    str, Depends(OAuth2PasswordBearer(tokenUrl="api/auth/login"))
]


class LoginToken(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str


class RefreshRequest(BaseModel):
    refresh_token: str
