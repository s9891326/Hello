# import os
#
# import pytest
# from dotenv import load_dotenv
# from starlette.testclient import TestClient
#
#
# @pytest.fixture(scope="class", autouse=True)
# def setup():
#     print("setup!!!!!!!!!!!!!!!!!")
#     load_dotenv("../setting/.env.dev")
#     os.environ["DB_TYPE"] = "mysql"
#     os.environ["RUN_MODE"] = "ASYNC"
#
#
# @pytest.fixture()
# def client():
#     from hello_fastapi.follow_ithelp.main import app
#
#     return TestClient(app)
#
#
# # @pytest.mark.usefixtures("setup")
# class TestCrudApi:
#     def test_hello(self, client):
#         result = client.get("/")
#         print(result)
#
#     @pytest.mark.parametrize(
#         "endpoint,message",
#         [
#             ("/hello", "4444"),
#         ],
#     )
#     def test_invalid_context_dependency(self, client, endpoint, message):
#         with pytest.raises(Exception) as exc_info:
#             client.get(endpoint)
#         print(str(exc_info.value))
#         assert str(exc_info.value) == message
#
#
# if __name__ == "__main__":
#     pytest.main()
import json
import os
import random
from functools import lru_cache

import pytest


@lru_cache()
def get_user_data():
    with open("data/user_data.json") as f:
        data = json.load(f)
    return data


def get_random_user():
    return [random.choice(get_user_data())]


@pytest.mark.asyncio
async def test_users(async_client):
    print(f"os!!!!!!!!!: {os.getenv('DB_TYPE')} {async_client}")
    response = await async_client.get("/api/users")
    assert response.status_code == 200


# @pytest.mark.asyncio
# async def test_create_user(async_client, get_user_data):
#     user = random.choice(get_user_data)
#     response = await async_client.post("api/users", json=user)
#
#     assert response.status_code == 201
#     assert response.json()["name"] == user["name"]
#     assert response.json()["email"] == user["email"]

async def get_user_id(async_client, user):
    response = await async_client.get(f"/api/users?last=0&limit=50&keyword={user['name']}")
    print(response.content)

    assert response.status_code == 200
    return response.json()[0]["id"]


@pytest.mark.parametrize("user", get_random_user())
@pytest.mark.asyncio
async def test_create_user(async_client, user):
    response = await async_client.post("/api/users", json=user)
    print(response.content)

    assert response.status_code == 201
    assert response.json()["name"] == user["name"]
    assert response.json()["email"] == user["email"]
    assert response.json()["id"] == await get_user_id(async_client, user)

# if __name__ == '__main__':
#     pytest.test()
