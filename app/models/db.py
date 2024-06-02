from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.ext.declarative import declarative_base

from models.dto import GetUser

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    email = Column("email", String(256), unique=True)
    password = Column("password", String(256))

    def to_GetUser(self) -> GetUser:
        return GetUser(
            id=self.id,
            email=self.email
        )
