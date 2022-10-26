from typing import List

from sqlalchemy.orm import Session

from hello_fastapi.models import User
from hello_fastapi.schemas import UserUpdate, UserBase, UserType


def get_users(db: Session, _skip: int, _limit: int) -> List[UserType]:
    return db.query(User).offset(_skip).limit(_limit).all()

def get_user_by_id(db: Session, _id: int):
    return db.query(User).filter_by(id=_id).first()

def create_user(db: Session, _create_data: UserBase) -> User:
    user_detail = db.query(User).filter_by(**_create_data.dict()).first()
    
    if user_detail:
        return user_detail
    # 轉化 pydantic model to orm model
    created_user = User(**_create_data.dict())

    # add instance object into database session
    # 增加 user orm model 所建立的 instance 到 database session
    db.add(created_user)
    
    # 提交 transaction to database (該 instance 會確實保存在 database)
    db.commit()
    # refresh instance (從 database 抽取該 instance 資料)
    db.refresh(created_user)
    return created_user
