from sqlalchemy import Delete
from sqlalchemy import Update
from models.db import User, UserEntity

from db.context import session_maker


def add(email: str, password: str) -> UserEntity:
    with session_maker.begin() as session:
        user = User()
        user.email = email
        user.password = password

        session.add(user)
        session.flush()

        return user.to_UserEntity()


def update(id: int, email: str, password: str) -> None:
    with session_maker.begin() as session:
        session.execute(Update(User).where(User.id == id).values({
            User.email: email,
            User.password: password,
        }))


def delete(id: int) -> None:
    with session_maker.begin() as session:
        session.execute(Delete(User).where(User.id == id))


def get_by_id(id: int) -> User | None:
    with session_maker() as session:
        return session.query(User).where(
            User.id == id
        ).first()


def get_by_email(email: str) -> UserEntity | None:
    with session_maker.begin() as session:
        result: User = session.query(User).where(
            User.email == email
        ).first()

        if result is None:
            return None

        return result.to_UserEntity()
