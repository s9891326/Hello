from fastapi import FastAPI
from sqlalchemy import text

from api.users import router as users_router
from api.items import router as items_router
from database.fake_db import get_db
from hello_fastapi.follow_ithelp.database.generic import get_db2, init_db
from setting.config import get_settings

app = FastAPI()
app.include_router(users_router)
app.include_router(items_router)

fake_db = get_db()


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/info")
def get_info():
    databases = None
    settings = get_settings()
    db_session = get_db2()

    try:
        databases = db_session.execute(
            text("SELECT datname FROM pg_database;")
        ).fetchall()
    except Exception as e:
        print(e)

    if databases is None:
        try:
            databases = db_session.execute(text("SHOW DATABASES;")).fetchall()
        except Exception as e:
            print(e)

    return {
        "app_name": settings.app_name,
        "author": settings.author,
        "app_mode": settings.app_mode,
        "port": settings.port,
        "reload": settings.reload,
        "db_type": settings.db_type,
        "database_url": settings.database_url,
        "database": str(databases),
    }
