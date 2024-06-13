from pydantic import BaseModel
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.ext.declarative import declarative_base

from utils.read_image import read_image

Base = declarative_base()

# USER


class UserEntity(BaseModel):
    id: int | None
    email: str | None
    password: str | None


class User(Base):
    __tablename__ = 'users'

    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    email = Column("email", String(256), unique=True)
    password = Column("password", String(256))

    def to_UserEntity(self) -> UserEntity:
        return UserEntity(
            id=self.id,
            email=self.email,
            password=self.password
        )

# IMAGE


class ImageEntity(BaseModel):
    id: int
    user_id: int
    name: str
    image: str
    created_at: datetime


class Image(Base):
    __tablename__ = 'images'

    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    user_id = Column("user_id", Integer(), ForeignKey('users.id'))
    name = Column("name", String(256))
    location = Column("location", String(256))
    created_at = Column("created_at", DateTime())

    def to_ImageEntity(self) -> ImageEntity:
        path = self.location + '/' + self.name
        image_base64 = read_image(path=path)
        return ImageEntity(
            id=self.id,
            user_id=self.user_id,
            name=self.name,
            image=image_base64,
            created_at=self.created_at
        )

# TOKEN


class TokenEntity(BaseModel):
    user_id: int
    hash: str
    expired_at: datetime
    created_at: datetime
