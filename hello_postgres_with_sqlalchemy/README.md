## Sqlalchemy + Postgresql ORM CRUD方式

### 建立連線
- `hello_postgres_with_sqlalchemy/database.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<server:port>/<db_name>"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
db = SessionLocal()

Base = declarative_base()  # inherit from this class to create ORM models

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
```
- `SQLALCHEMY_DATABASE_URL`以`PostgreSQL`格式為例，如果使用不同種類的資料庫，要改為相對應的連線字串
- 透過`create_engine`來建立資料庫的連線，`sessionmaker`則是建立連線會話
- `echo=True`是可以顯示SQL操作了何種語法
> 要特別注意 sqlalchemy `不允許修改表結構`，如果需要修改的話，需要刪除重建
- `autoflush(default: True)`:
  - 解釋: 把當前session存在的變更發給DB => 讓DB執行SQL語法
  - True: 會把當前操作的SQL發送給DB執行，所以可以在相同的事務裡面查到上一個sql新增的資料
  - False: 不會把累積的SQL發送給DB，當前的查詢操作也查不到上一個sql新增的資料
- `autocommit(default: False)`:
  - 解釋: 是否自動提交事務，一個事務裡面可能有一條或多條SQL語法。default是每個請求開啟了事務，並且要手動提交事務
  - True: 就不會開啟事務了，所以需要手動flush，告訴DB執行甚麼
  - False: 全部請求都開啟事務，每次結束SQL語法時，加上`db.commit()`
- `Base`是SQLAlchemy model的基礎類別，透過繼承它來建立表格的model
- 建立`get_db_session()`並實現一個 database session instance and yield it

### 建立model
- `hello_postgres_with_sqlalchemy/models.py`
```python
from sqlalchemy import Column, Integer, String

from hello_postgres_with_sqlalchemy.database import Base, engine

class Test(Base):
  __tablename__ = "test_table"  # 資料表名稱

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(55))
  age = Column(Integer)

  def __str__(self):
    return f"Test<id={self.id}, name={self.name}, age={self.age}>"

def create_table():
  Base.metadata.create_all(engine)

def drop_table():
  Base.metadata.drop_all(engine)

# if __name__ == '__main__':
#   # 因為sqlalchemy無法更新資料表，所以需要刪掉重創
#   drop_table()
#   create_table()
```
- 對DB創建了一張新的table=`test_table`，使用`Column`來定義SQL表中的欄位

### CRUD
- `hello_postgres_with_sqlalchemy/crud.py`
```python
from sqlalchemy.orm import Session
from hello_postgres_with_sqlalchemy.database import get_db_session
from hello_postgres_with_sqlalchemy.models import Test

# 新增
def create_test(db: Session, test_data: dict) -> Test:
    created_test = Test(**test_data)
    db.add(created_test)
    db.commit()
    return created_test

# 讀取
def get_test_by_id(db: Session, test_id: int) -> Test:
    result = db.query(Test).filter_by(id=test_id).first()
    db.commit()
    return result

# 一次讀取100筆
def get_all_test(db: Session, skip: int = 0, limit: int = 100):
    result = db.query(Test).offset(skip).limit(limit).all()
    db.commit()
    return result

# 更新
def update_test(db: Session, test_id: int, _update_data: dict) -> int:
    r = db.query(Test).filter_by(id=test_id).update(_update_data)
    db.commit()
    return r

# 刪除
def delete_test(db: Session, test_id: int) -> int:
    r = db.query(Test).filter_by(id=test_id).delete()
    db.commit()
    return r

if __name__ == '__main__':
    _db = next(get_db_session())
    
    print(len(get_all_test(_db)))  # 6
    
    data = {"name": "hello", "age": 18}
    test_data = create_test(_db, data)
    print(test_data)                          # Test<id=10, name=hello, age=18>
    print(get_test_by_id(_db, test_data.id))  # Test<id=10, name=hello, age=18>

    update_data = {"name": "hello2", "age": Test.age + 5}
    print(update_test(_db, test_data.id, update_data))  # 1
    print(len(get_all_test(_db)))  # 7
    print(get_test_by_id(_db, test_data.id))   # Test<id=10, name=hello2, age=23>
    
    print(delete_test(_db, test_data.id))      # 1
    print(get_test_by_id(_db, test_data.id))   # None
    print(len(get_all_test(_db)))  # 6

    
```
- 透過`sqlalchemy.orm`的`Session`，對不同的SQL表進行query
- 如果只要查詢單一數據行，使用`first()`、如果要回傳所有符合條件的數據，使用`all()`
- `add`此實例物件到資料庫`session`

### Postgresql command line 語法
- `select * from pg_stat_activity;`: 等於mysql `show processlist` 查看當前有哪些process在執行
- `psql -U <username>`: 登入方式
- `\l`: show all database
- `\c <database_name>`: choose your database
- `\dt`: show all tables in current database 

### Reference
- https://www.jianshu.com/p/b219c3dd4d1e
- https://medium.com/@kevinwei30/sqlalchemy-in-python-with-postgresql-d965ca20de59
