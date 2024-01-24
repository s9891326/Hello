import pytest
import redis
import redis.asyncio as redis_async
from redis_om import get_redis_connection
from typing import Optional
from redis_om import HashModel, Field, Migrator

REDIS_URL = "redis://localhost:6379"
connection_pool = redis.ConnectionPool.from_url(REDIS_URL)
connection_pool2 = redis_async.ConnectionPool.from_url(REDIS_URL)
redis_om_connect = get_redis_connection(url=REDIS_URL)


def test_redis_connection():
    redis_connect = redis.Redis.from_url(REDIS_URL)

    value = "bar"
    redis_connect.set("foo", value)
    result = redis_connect.get("foo")
    redis_connect.close()
    assert result.decode() == value


def test_redis_connection_pool():
    redis_connect = redis.Redis(connection_pool=connection_pool)

    value = "bar2"
    redis_connect.set("foo2", value)
    result = redis_connect.get("foo2")
    redis_connect.close()
    assert result.decode() == value


@pytest.mark.asyncio
async def test_redis_async_connection():
    redis_connect = redis_async.Redis.from_url(REDIS_URL)

    value = "boo"
    await redis_connect.set("foo_async", value)
    result = await redis_connect.get("foo_async")
    redis_connect.close()

    assert result.decode() == value


@pytest.mark.asyncio
async def test_redis_async_connection_pool():
    redis_connect = redis_async.Redis(connection_pool=connection_pool2)

    value = "bar_async2"
    await redis_connect.set("foo_async2", value)
    value = await redis_connect.get("foo_async2")
    redis_connect.close()

    assert value.decode() == "bar_async2"


Migrator().run()


class UserReadCache(HashModel):
    id: int = Field(index=True)
    name: str = Field(index=True)
    email: str = Field(index=True)
    avatar: Optional[str] = None

    class Meta:
        database = redis_om_connect


def test_create_user():
    new_user = UserReadCache(id=1, name="eddy", email="a@email.com", avatar="image_url")
    new_user.save()
    pk = new_user.pk
    assert UserReadCache.get(pk) == new_user


def test_find_user_hash():
    user_be_found = UserReadCache(
        id=1, name="eddy", email="json_user@email.com", avatar="image_url"
    )
    result = UserReadCache.find(UserReadCache.id == 1).first()
    assert result.id == user_be_found.id
    assert result.name == user_be_found.name
