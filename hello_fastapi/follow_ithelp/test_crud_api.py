import os

import pytest
from dotenv import load_dotenv
from starlette.testclient import TestClient


@pytest.fixture(scope="class", autouse=True)
def setup():
    print("setup!!!!!!!!!!!!!!!!!")
    load_dotenv("setting/.env.dev")
    os.environ["DB_TYPE"] = "mysql"
    os.environ["RUN_MODE"] = "ASYNC"


@pytest.fixture()
def client():
    from hello_fastapi.follow_ithelp.main import app

    return TestClient(app)


# @pytest.mark.usefixtures("setup")
class TestCrudApi:
    def test_hello(self, client):
        result = client.get("/")
        print(result)

    @pytest.mark.parametrize(
        "endpoint,message",
        [
            ("/hello", "4444"),
        ],
    )
    def test_invalid_context_dependency(self, client, endpoint, message):
        with pytest.raises(Exception) as exc_info:
            client.get(endpoint)
        print(str(exc_info.value))
        assert str(exc_info.value) == message


if __name__ == "__main__":
    pytest.main()
