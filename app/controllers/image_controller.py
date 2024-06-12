import io
from fastapi import APIRouter, Depends
from fastapi import File, UploadFile, status
from fastapi.responses import Response

from core.middleware.auth_middleware import auth_middleware
from services import image_service

router = APIRouter(
    prefix="/image",
    tags=["Image"],
    dependencies=[Depends(auth_middleware)]
)


@router.post("/", status_code=status.HTTP_200_OK)
def improve_image(file: UploadFile = File(...)):
    img_byte_arr = io.BytesIO()
    result = image_service.improve_image(file=file)
    result.save(img_byte_arr, format='JPEG')

    return Response(content=img_byte_arr.getvalue(), media_type='image/png')


@router.post("/save_image", status_code=status.HTTP_201_CREATED)
async def save_image(file: UploadFile = File(...)):
    return "Save Image"


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_image(id: int):
    pass


@router.get("/", status_code=status.HTTP_200_OK)
def get_images():
    pass


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_image(id: int):
    pass
