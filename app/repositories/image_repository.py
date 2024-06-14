from datetime import datetime

from core.constants.constants import PATH
from db.context import session_maker
from fastapi import UploadFile
from models.db import Image, ImageEntity, User
from sqlalchemy import Delete
from utils import delete_image
from utils.save_image import save_image
from utils.verify_folder import verify_folder


def add(user: User, file: UploadFile):
    fileName = file.filename.replace(' ', '')
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = timestamp + fileName
    path = PATH + user.email

    # TODO: Se debe agregar un try y catch para tener el control de la crear cion de folders
    verify_folder(path=path)
    save_image(path=path, file=file, filename=new_filename)

    with session_maker.begin() as session:
        image = Image()
        image.location = path
        image.user_id = user.id
        image.name = new_filename
        image.created_at = datetime.now().date()

        session.add(image)
        session.flush()


def get_by_id(id: int) -> ImageEntity:
    with session_maker.begin() as session:
        return session.query(Image).where(
            Image.id == id
        ).first().to_ImageEntity()


def get_images_by_user_id(user_id: int, limit: int = 1000, offset: int = 0) -> list[ImageEntity]:
    images = []
    with session_maker.begin() as session:
        list_image = session.query(Image).where(
            Image.user_id == user_id
        ).limit(limit).offset(offset).all()

        for image in list_image:
            images.append(image.to_ImageEntity())

        return images


def delete(id: int) -> None:
    with session_maker.begin() as session:
        image = session.query(Image).where(
            Image.id == id
        ).first()
        path = image.location + '/' + image.name
        delete_image.delete_image(path=path)
        session.execute(Delete(Image).where(Image.id == id))
