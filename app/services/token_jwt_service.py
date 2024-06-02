from datetime import datetime

import jwt

from models import db
from models import dto

SECRET_KEY = "SECRET_KEY"
ALGORITHM = "HS256"


def create(user_id: int, exp: datetime) -> str:
    token = dto.Token(
        id=user_id,
        expired_at=exp
    )

    return jwt.encode(token.model_dump(), SECRET_KEY, algorithm=ALGORITHM)


def parse(token: str) -> dto.Token:
    try:
        token_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return dto.Token(**token_data)
    except jwt.PyJWTError as e:
        print(e)
        return None
