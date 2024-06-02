from datetime import datetime
from datetime import timezone

from fastapi import status
from fastapi import Response
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from utils import formating
from models import dto
from services import user_service, token_service

COOKIES_KEY_NAME = "session_token"

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=dto.GetUser)
def register(user: dto.CreateUser):
    email = formating.format_string(user.email)

    if not email:
        raise HTTPException(
            detail="Email can not be empty",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    if not user.password:
        raise HTTPException(
            detail="Password can not be empty",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    exist_user = user_service.get_by_email(email=email)
    if exist_user:
        raise HTTPException(
            detail=f"User '{email}' exist",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    return user_service.create(
        email=user.email,
        password=user.password
    )


@router.post("/login", status_code=status.HTTP_200_OK, response_model=dto.Token)
def login(dto: dto.LoginUser, res: Response):
    email = formating.format_string(dto.email)

    user = user_service.get_by_email_and_password(
        email=email,
        password=dto.password
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    token_service.delete_expired(user_id=user.id)

    token = token_service.create(user_id=user.id)
    token_exp_date: datetime = token.expired_at
    res.set_cookie(
        COOKIES_KEY_NAME,
        token.hash,
        expires=token_exp_date.replace(tzinfo=timezone.utc)
    )

    return token


@router.get("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(req: Request) -> JSONResponse:
    token_hash = req.cookies.get(COOKIES_KEY_NAME)

    if token_hash is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sesion not found"
        )

    token_service.delete_by_hash(hash=token_hash)
