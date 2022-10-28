# assume create a test.py, and write in
# import database session, user orm model, user pydantic model
from hello_fastapi.crud import create_user
from hello_fastapi.database import get_db_session
# import fastapi special encoder jsonable_encoder
from fastapi.encoders import jsonable_encoder

from hello_fastapi.models import User
from hello_fastapi.schemas import UserUpdate, UserBase


def orm_to_pydantic(orm_model):
    """將 ORM model 的資料搬移到 Pydantic model"""
    # 1. convert orm model to json format by jsonable_encoder
    # 2. unwrapped jsonable query_result into UserSchema(as user pydantic model)
    jsonable_result = jsonable_encoder(orm_model)
#     return UserSchema(**jsonable_result)


def pydantic_to_orm(pydantic_model):
    """將 Pydantic model 的資料搬移到 ORM model"""
    return User(**pydantic_model.dict())


def query_user():
    # get database session, it will return generator first
    db = next(get_db_session())
    # execute database query, the result is a list of user orm model
    users_orm_model = db.query(User).all()
    print(users_orm_model)
    
    # user_pydantic_model = [orm_to_pydantic(user_orm_model) for user_orm_model in users_orm_model]
    # print(user_pydantic_model)


def create_user():
    # user = UserSchema(id=1, name="eddy", email="eddy@gmail.com", active=True, books=[])
    user = User(name='ed', fullname='ED Jones', nickname='edsnickname')
    
    db = next(get_db_session())
    # db.add(user)
    db.add_all([
        User(name='ed1', fullname='ED Jones', nickname='edsnickname'),
        User(name='ed2', fullname='ED Jones', nickname='edsnickname'),
        User(name='ed3', fullname='ED Jones', nickname='edsnickname')
    ])
    print('the result of user is before commit(): ', db.query(User).count())
    
    db.rollback()
    print('the result of user is after rollback(): ', db.query(User).count())
    
    db.commit()
    print('the result of user is after commit(): ', db.query(User).count())
    
    # user = db.query(User).filter_by(name="ed1").first()
    # print(user)


def create_user2():
    user = UserBase(name="eddy", fullname="wang", nickname="nick")
    db = next(get_db_session())
    result = create_user(db, user)
    print(result)

if __name__ == '__main__':
    # create_user()
    create_user2()
    # query_user()
