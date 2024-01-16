from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from hello_fastapi.follow_ithelp.auth.passwd import get_password_hash
from hello_fastapi.follow_ithelp.database.generic import get_db2
from hello_fastapi.follow_ithelp.models.users import User
from hello_fastapi.follow_ithelp.schemas import users as UserSchema


class UserCrudManager:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_user_id_by_email(self, email: str):
        stmt = select(User.id).where(User.email == email)
        result = await self.db_session.execute(stmt)
        user = result.first()

        if user:
            return user
        return None

    async def create_user(self, new_user: UserSchema.UserCreate):
        new_user.password = get_password_hash(new_user.password)
        user = User(
            name=new_user.name,
            password=new_user.password,
            age=new_user.age,
            birthday=new_user.birthday,
            email=new_user.email,
            avatar=new_user.avatar,
        )

        self.db_session.add(user)
        await self.db_session.commit()
        # await self.db_session.refresh(user)

        return user

    async def get_users(self, keyword: str = None, last: int = 0, limit: int = 50):
        stmt = select(User.name, User.id, User.email, User.avatar)
        if keyword:
            stmt = stmt.where(User.name.like(f"%{keyword}%"))
        stmt = stmt.offset(last).limit(limit)
        result = await self.db_session.execute(stmt)
        users = result.all()

        return users

    async def get_user_by_username(self, username: str):
        stmt = select(User.id, User.name, User.password, User.email, User.avatar).where(User.name == username)
        result = await self.db_session.execute(stmt)
        user = result.first()

        if user:
            return user
        return None

    async def check_user_id(self, user_id: str) -> Optional[str]:
        stmt = select(User.id).where(User.id == user_id)
        result = await self.db_session.execute(stmt)
        user = result.first()

        if user:
            return user.id
        return None

    async def update_user(self, user_id: str, update_column: dict):
        stmt = update(User).where(User.id == user_id).values(update_column)
        await self.db_session.execute(stmt)

        stmt = select(User.id, User.name, User.avatar, User.age, User.birthday).where(
            User.id == user_id
        )
        result = await self.db_session.execute(stmt)
        await self.db_session.commit()
        return result.first()


async def get_user_crud_manager():
    async with get_db2() as db_session:
        yield UserCrudManager(db_session)