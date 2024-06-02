from os import getenv  # El getenv me esta dando error, seria bueno ver el por que?
from typing import Generator
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from models.db import Base


CONNECTION_STRING = "sqlite:///./sql_app.db"
if not CONNECTION_STRING:
    raise Exception("DB connection string not provided")

engine = create_engine(
    CONNECTION_STRING,
    connect_args={"check_same_thread": False}
)
session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db() -> None:
    """
    Creates the database tables by calling `Base.metadata.create_all(engine)`.
    """
    Base.metadata.create_all(engine)


def get_db() -> Generator[Session, Any, None]:
    """
    Returns a generator that yields a SQLAlchemy session. This session should be used for all database interactions within the current request context.
    """
    with session_maker() as session:
        yield session


def auto_create_db():
    """
    Automatically creates the database if it doesn't already exist.

    This function attempts to connect to the database engine. If an exception is raised, it means the database doesn't exist yet, so it creates the database using the connection string and database name extracted from the `CONNECTION_STRING` variable.

    After creating the database, it calls the `create_db()` function to perform any additional setup or initialization for the database.
    """
    try:
        con = engine.connect()
        con.close()

    except Exception as _:
        connection_string, db_name = CONNECTION_STRING.rsplit("/", 1)

        tmp_engine = create_engine(connection_string)
        with tmp_engine.begin() as session:
            session.exec_driver_sql(f"CREATE DATABASE `{db_name}`")

        create_db()
