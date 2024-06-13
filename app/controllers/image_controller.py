import io

from core.middleware.auth_middleware import auth_middleware
from fastapi import APIRouter, Depends, File, Request, UploadFile, status
from fastapi.responses import Response
from models import dto
from services import image_service
from services.token_jwt_service import parse

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
async def save_image(req: Request, file: UploadFile = File(...)):
    token = req.headers['bearerToken']
    parse_token: dto.Token = parse(token=token)

    image_service.create(user_id=parse_token.user_id, file=file)

    return "Save Image"


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_image(id: int):
    pass


@router.get("/", status_code=status.HTTP_200_OK)
def get_images(req: Request):
    token = req.headers['bearerToken']
    parse_token: dto.Token = parse(token=token)

    return image_service.get_images_by_user_id(user_id=parse_token.user_id)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_image(id: int):
    pass
