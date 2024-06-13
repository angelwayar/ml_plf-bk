from fastapi import FastAPI

from controllers import auth_controller
from controllers import image_controller

app = FastAPI()

app.include_router(auth_controller.router)
app.include_router(image_controller.router)
