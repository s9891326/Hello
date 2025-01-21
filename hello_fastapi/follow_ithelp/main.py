from fastapi import FastAPI
from sqlalchemy import text

from hello_fastapi.follow_ithelp.setting.config import get_settings

settings = get_settings()
app = FastAPI()

if settings.run_mode == "ASYNC":
    from hello_fastapi.follow_ithelp.api.users import router as users_router
    from hello_fastapi.follow_ithelp.api.items import router as items_router
    from hello_fastapi.follow_ithelp.api.auth import router as auth_router
    from hello_fastapi.follow_ithelp.database.generic import get_db2, init_db, close_db

    app.include_router(users_router)
    app.include_router(items_router)
    app.include_router(auth_router)

    @app.on_event("startup")
    async def startup():
        await init_db()

    @app.on_event("shutdown")
    async def shutdown():
        await close_db()

else:
    from hello_fastapi.follow_ithelp.sync.api.users import router as users_router
    from hello_fastapi.follow_ithelp.sync.api.items import router as items_router
    from hello_fastapi.follow_ithelp.database.generic import get_db2, init_db

    app.include_router(users_router)
    app.include_router(items_router)

    @app.on_event("startup")
    def startup():
        init_db()

    @app.on_event("shutdown")
    def shutdown():
        close_db()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/hello")
def hello():
    raise Exception("4444")


@app.get("/info")
def get_info():
    databases = None
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
