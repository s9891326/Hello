from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@192.168.223.127:5432/test"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    pool_size=8,
    connect_args={'connect_timeout': 3}
)
# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # inherit from this class to create ORM models


# 建立 get_db_session() 並實現一個 database session instance and yield it
def get_db_session():
    session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    db = session()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
