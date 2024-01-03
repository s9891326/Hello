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


# @pytest.mark.usefixtures("setup")
class TestCrudApi:
    def test_hello(self):
        from hello_fastapi.follow_ithelp.main import app
        client = TestClient(app)
        result = client.get("/")
        print(result)


if __name__ == '__main__':
    pytest.main()
