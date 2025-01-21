from datetime import date
from typing import Optional

import redis
import redis.asyncio as redis_async
from redis_om import get_redis_connection, JsonModel, Field

from hello_fastapi.follow_ithelp.setting.config import get_settings

settings = get_settings()

redis_om_connect = get_redis_connection(url=settings.redis_url)
# redis_om_connect = get_redis_connection(url=REDIS_URL)
redis_pool = redis_async.ConnectionPool.from_url(settings.redis_url)


class UserCache(JsonModel):
    id: Optional[int] = Field(index=True)
    name: Optional[str] = Field(index=True)
    password: Optional[str] = Field(index=True)
    avatar: Optional[str] = Field(index=True)
    age: Optional[int] = Field(index=True)
    email: Optional[str] = Field(index=True)
    birthday: Optional[date] = Field(index=True)

    class Meta:
        database = redis_om_connect


def generic_cache_get(prefix: str, key: str, cls: object):
    """
    prefix: namespace for redis key ( such as `user` 、`item` 、`article` )
    key: **parameter name** in caller function ( such as `user_id` 、`email` 、`item_id` )
    cls: **response schema** in caller function ( such as `UserSchema.UserRead`、`UserSchema.UserId`、`ItemSchema.ItemRead`)
    """

    rc = redis.Redis(connection_pool=redis_pool)

    def inner(func):
        async def wrapper(*args, **kwargs):
            value_key = kwargs.get(key)
            if not value_key:
                return await func(*args, **kwargs)

            cache_key = f"{prefix}:{value_key}"

            redis_result = rc.hgetall(cache_key)
            if redis_result:
                return cls(**redis_result)

            sql_result = await func(*args, **kwargs)
            if not sql_result:
                return None

            rc.hset(cache_key, sql_result)
            return sql_result

        return wrapper

    return inner
