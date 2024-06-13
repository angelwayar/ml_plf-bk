from models import db
from repositories import user_repository

from utils import hashing
from utils import formating


def create(email: str, password: str) -> db.User:
    email = formating.format_string(email)
    password = hashing.hash_password(password)

    return user_repository.add(email=email, password=password)


def get_by_id(id: int) -> db.User | None:
    return user_repository.get_by_id(id=id)


def get_by_email(email: str) -> db.User | None:
    return user_repository.get_by_email(email=email.lower().strip())


def get_by_email_and_password(email: str, password: str) -> db.User | None:
    result = None

    pass_hash = hashing.hash_password(password=password)
    user = user_repository.get_by_email(email=email)

    if user and user.password == pass_hash:
        result = user
        result.password = None

    return result


def update(id: int, email: str, password: str) -> None:
    email = formating.format_string(email)
    password = (password)
    user_repository.update(id=id, email=email, password=password)


def update_password(id: int, old_password: str, new_password: str) -> None:
    user = get_by_email(id)
    if user is None:
        return

    old_pass_hash = hashing.hash_password(old_password)
    if user.password != old_pass_hash:
        return

    new_pass_hash = hashing.hash_password(new_password)
    user_repository.update(
        id=user.id,
        email=user.email,
        password=new_pass_hash
    )


def delete(id: int) -> None:
    user_repository.delete(id=id)
