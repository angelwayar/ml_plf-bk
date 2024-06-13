from datetime import datetime

import tensorflow as tf
from db.context import session_maker
from fastapi import UploadFile
from models import db
from models.db import User
from PIL import Image
from repositories import image_repository
from utils.read_image import read_image
from utils.save_image import save_image

IMG_HEIGHT = 256
IMG_WIDTH = 256


def create(user_id: int, file: UploadFile) -> db.Image:
    user = get_by_id(id=user_id)
    return image_repository.add(user=user, file=file)


def get_image_by_id(id: int) -> db.ImageEntity | None:
    return image_repository.get_by_id(id=id)


def get_images_by_user_id(user_id: int) -> list[db.ImageEntity] | None:
    return image_repository.get_images_by_user_id(user_id=user_id)


def delete(id: int) -> None:
    image_repository.delete(id=id)


def improve_image(file: UploadFile):
    img = Image.open(file.file)

    input_api = tf.cast(img, tf.float32)[..., :3]
    resize_img = tf.image.resize(input_api, [IMG_WIDTH, IMG_HEIGHT])
    input_api_normalize = (resize_img / 127.5) - 1

    dimensions = tf.expand_dims(input_api_normalize, axis=0)

    model = tf.saved_model.load("core/ai_models").signatures['predict1']

    result = model(dimensions)['outputs']
    img_r = (result + 1) / 2

    new_img = tf.keras.utils.array_to_img(img_r[0])

    return new_img


def get_by_id(id: int) -> User | None:
    with session_maker() as session:
        return session.query(User).where(
            User.id == id
        ).first()
