import os


def verify_folder(path: str):
    if not os.path.exists(path=path):
        try:
            os.makedirs(path)
            print(f"Directorio creado: {path}")
        except OSError as error:
            print(f"Error al crear el directorio: {error}")
