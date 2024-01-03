from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete

from hello_fastapi.follow_ithelp.sync.database.generic import get_db2
from hello_fastapi.follow_ithelp.models.users import User
from hello_fastapi.follow_ithelp.schemas import users as UserSchema

db_session: Session = get_db2()


def get_user_id_by_email(email: str):
    stmt = select(User.id).where(User.email == email)
    user = db_session.execute(stmt).first()
    if user:
        return user

    return None


def create_user(newUser: UserSchema.UserCreate):
    user = User(
        name=newUser.name,
        password=newUser.password,
        age=newUser.age,
        birthday=newUser.birthday,
        email=newUser.email,
        avatar=newUser.avatar,
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    return user


def get_users(keyword: str = None, last: int = 0, limit: int = 50):
    stmt = select(User.name, User.id, User.email, User.avatar)
    if keyword:
        stmt = stmt.where(User.name.like(f"%{keyword}%"))
    stmt = stmt.offset(last).limit(limit)
    users = db_session.execute(stmt).all()

    return users
