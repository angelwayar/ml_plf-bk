from datetime import datetime

from sqlalchemy import Delete

from models.db import Token, TokenEntity
from db.context import session_maker


def add(user_id: int, hash: str, valid_to: datetime) -> TokenEntity:
    with session_maker.begin() as session:
        token = Token()
        token.user_id = user_id
        token.hash = hash
        token.expired_at = valid_to

        session.add(token)
        session.flush()

        return token.to_TokenEntity()


def delete(id: int) -> None:
    with session_maker.begin() as session:
        session.execute(Delete(Token).where(Token.id == id))


def delete_by_user_id(id: int) -> None:
    with session_maker.begin() as session:
        session.execute(Delete(Token).where(Token.user_id == id))


def get_by_id(id: int) -> TokenEntity | None:
    with session_maker() as session:
        return session.query(Token).where(
            Token.id == id
        ).first().to_TokenEntity()


def get_by_user_id(user_id: int, limit: int = 1000, offset: int = 0) -> list[TokenEntity]:
    list_TokenEntity = []

    with session_maker() as session:
        list_token = session.query(Token).where(
            Token.user_id == user_id
        ).limit(limit).offset(offset).all()

        for token in list_token:
            list_TokenEntity.append(token.to_TokenEntity())

        return list_TokenEntity


def get_by_hash(obj_hash: str) -> TokenEntity | None:
    with session_maker() as session:
        return session.query(Token).where(
            Token.hash == obj_hash
        ).first().to_TokenEntity()
