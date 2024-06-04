import tensorflow as tf
from PIL import Image

from fastapi import UploadFile

from models import db
from repositories import image_repository

IMG_HEIGHT = 256
IMG_WIDTH = 256


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
