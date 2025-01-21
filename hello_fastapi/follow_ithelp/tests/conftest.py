# conftest.py 是 pytest 中一個特殊的檔案，可以讓我們在測試中使用一些共用的設定
import asyncio
import os

import pytest
import pytest_asyncio
from dotenv import load_dotenv
from httpx import AsyncClient



def pytest_addoption(parser):
    parser.addoption(
        "--prod", action="store_true", help="Run the server in production mode."
    )
    parser.addoption("--test", action="store_true", help="Run the server in test mode.")
    parser.addoption(
        "--dev", action="store_true", help="Run the server in development mode."
    )
    parser.addoption("--sync", action="store_true", help="Run the server in Sync mode.")
    parser.addoption(
        "--db",
        help="Run the server in database type.",
        choices=["mysql", "postgresql"],
        default="mysql",
    )


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


# function : 每個測試都會執行一次
# class : 每個測試類別都會執行一次
# module : 每個測試 module 都會執行一次
# session : 整個測試會執行一次
@pytest_asyncio.fixture(scope="session")
async def dependencies(request):
    args = request.config

    # 本機環境測試使用
    if args.getoption("prod"):
        load_dotenv("../setting/.env.prod")
    else:
        load_dotenv("../setting/.env.dev")

    # if args.getoption("prod"):
    #     load_dotenv("setting/.env.prod")
    # else:
    #     load_dotenv("setting/.env.dev")

    if args.getoption("sync"):
        os.environ["RUN_MODE"] = "SYNC"
    else:
        os.environ["RUN_MODE"] = "ASYNC"

    os.environ["DB_TYPE"] = args.getoption("db")
    print(f"dependencies!!!!! DB_TYPE: {os.getenv('DB_TYPE')}, {os.getenv('PORT')}")


@pytest_asyncio.fixture(scope="module")
async def async_client(dependencies) -> AsyncClient:
    print(f"async_client!!!!!!!!!! {os.getenv('DB_TYPE')}, {dependencies}, {os.getenv('PORT')}")
    from hello_fastapi.follow_ithelp.main import app

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
