import re
import shutil

from fastapi import UploadFile


def save_image(path: str, file: UploadFile, filename: str):
    new_path = path + '/' + re.sub(r'[^\w\-_\.]', '_', filename)

    print(f"el nuevo path es: {new_path}")
    try:
        with open(new_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except IOError as e:
        print(f"Error al guardar el archivo: {e}")
        raise
    finally:
        file.file.close()
