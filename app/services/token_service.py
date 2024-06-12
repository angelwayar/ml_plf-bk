from datetime import datetime
from datetime import timezone
from datetime import timedelta

from models import db
# from repositories import token_repository
from utils import hashing

SESSION_TTL = timedelta(days=7)


def create(user_id: int) -> db.TokenEntity:
    hash = hashing.generate_hash()
    valid_to = datetime.now(timezone.utc).replace(tzinfo=None) + SESSION_TTL

    return db.TokenEntity(
        user_id=user_id,
        hash=hash,
        expired_at=valid_to,
        created_at=datetime.now()
    )

# Quizas se deba de remover estas funciones del Token

# def get_by_id(id: int) -> db.Token | None:
#     return token_repository.get_by_id(id=id)


# def get_by_user_id(user_id: int) -> list[db.Token]:
#     return token_repository.get_by_user_id(user_id)


# def get_by_hash(hash: str) -> db.Token | None:
#     return token_repository.get_by_hash(hash)


# def delete(token_id: int) -> None:
#     token_repository.delete(token_id)


# def delete_by_hash(hash: str) -> None:
#     token = get_by_hash(hash)
#     if token:
#         delete(token.id)


# def delete_expired(user_id: int) -> None:
#     tokens = token_repository.get_by_user_id(user_id)
#     now = datetime.now(timezone.utc).replace(tzinfo=None)
#     for t in tokens:
#         if t.expired_at < now:
#             delete(t)
