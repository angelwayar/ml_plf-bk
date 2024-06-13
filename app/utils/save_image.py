import re
import shutil
from datetime import datetime

from fastapi import UploadFile


def save_image(path: str, file: UploadFile):
    fileName = file.filename.replace(' ', '')
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = timestamp + fileName
    new_path = path + '/' + re.sub(r'[^\w\-_\.]', '_', new_filename)

    print(f"el nuevo path es: {new_path}")
    try:
        with open(new_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except IOError as e:
        print(f"Error al guardar el archivo: {e}")
        raise
    finally:
        file.file.close()
