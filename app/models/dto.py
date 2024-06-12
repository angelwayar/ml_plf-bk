from datetime import datetime
from pydantic import BaseModel

# USER


class CreateUser(BaseModel):
    email: str
    password: str


class GetUser(BaseModel):
    id: int
    email: str


class UpdateUser(BaseModel):
    email: str

# Image


class CreateImage(BaseModel):
    user_id: int
    name: str
    location: str


class GetImage(BaseModel):
    id: int
    user_id: int
    name: str
    location: str
    created_at: datetime

# LOGIN


class LoginUser(BaseModel):
    email: str
    password: str


# TOKEN


class Token(BaseModel):
    user_id: int
    hash: str
    created_at: datetime
    expired_at: datetime


class CreateToken(BaseModel):
    user_id: int
    hash: str
    created_at: str
    expired_at: str


class BearerToken(BaseModel):
    bearer_token: str
