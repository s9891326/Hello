from datetime import datetime, timedelta

from fastapi import HTTPException
from jose import jwt, ExpiredSignatureError, JWTError
from starlette import status

from hello_fastapi.follow_ithelp.setting.config import get_settings
from hello_fastapi.follow_ithelp.schemas.auth import LoginToken, RefreshRequest

settings = get_settings()

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


async def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=settings.access_token_expire_minutes)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.access_token_secret)
    return encoded_jwt


async def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=settings.refresh_token_expire_minutes)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.refresh_token_secret)
    return encoded_jwt


async def create_token_pair(access_data: dict, refresh_data: dict) -> LoginToken:
    access_token = await create_access_token(access_data)
    refresh_token = await create_refresh_token(refresh_data)
    return LoginToken(
        access_token=access_token, refresh_token=refresh_token, token_type="bearer"
    )


async def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.access_token_secret)
        return payload
    except ExpiredSignatureError:
        raise credentials_exception
    except JWTError:
        raise credentials_exception


async def verify_refresh_token(token: str):
    try:
        payload = jwt.decode(token, settings.refresh_token_secret)
        return payload
    except ExpiredSignatureError:
        raise credentials_exception
    except JWTError:
        raise credentials_exception
