from sqlalchemy.orm import Session

from hello_postgres_with_sqlalchemy.database import get_db_session
from hello_postgres_with_sqlalchemy.models import Test


def get_all_test(db: Session, skip: int = 0, limit: int = 100):
    result = db.query(Test).offset(skip).limit(limit).all()
    db.commit()
    return result


def get_test_by_id(db: Session, test_id: int):
    result = db.query(Test).filter_by(id=test_id).first()
    db.commit()
    return result


def create_test(db: Session, test_data: dict) -> Test:
    created_test = Test(**test_data)
    db.add(created_test)
    db.commit()
    return created_test


def update_test(db: Session, test_id: int, update_data: dict) -> int:
    r = db.query(Test).filter_by(id=test_id).update(update_data)
    db.commit()
    return r


def delete_test(db: Session, test_id: int) -> int:
    r = db.query(Test).filter_by(id=test_id).delete()
    db.commit()
    return r


if __name__ == '__main__':
    _db = next(get_db_session())
    # print(len(get_all_test(_db)))

    data = {"name": "hello", "age": 182}
    test_data = create_test(_db, data)
    print(test_data)
    # print(get_test_by_id(_db, test_data.id))

    # update_data = {"name": "hello2", "age": Test.age + 5}
    # print(update_test(_db, test_data.id, update_data))
    #
    # print(get_test_by_id(_db, test_data.id))
    # print(delete_test(_db, test_data.id))
    # print(get_test_by_id(_db, test_data.id))


