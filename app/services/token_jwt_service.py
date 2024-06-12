import jwt

from models import dto

SECRET_KEY = "SECRET_KEY"
ALGORITHM = "HS256"


def create(token: dto.Token) -> str:
    create_token = dto.CreateToken(
        user_id=token.user_id,
        hash=token.hash,
        created_at=str(token.created_at),
        expired_at=str(token.expired_at),)

    return jwt.encode(create_token.model_dump(), SECRET_KEY, algorithm=ALGORITHM)


def parse(token: str) -> dto.Token:
    try:
        token_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return dto.Token(**token_data)
    except jwt.PyJWTError as e:
        print(e)
        return None
