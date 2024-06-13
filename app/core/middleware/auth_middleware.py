from datetime import datetime

from fastapi import HTTPException, Request, status
from models import dto
from services.token_jwt_service import parse
from services.user_service import get_by_id


async def auth_middleware(req: Request):
    try:
        token = req.headers["bearerToken"]
        object_token: dto.Token = parse(token=token)
        user = get_by_id(id=object_token.user_id)

        if object_token.expired_at < datetime.now() and user is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token expired"
            )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Problem with the token"
        )
