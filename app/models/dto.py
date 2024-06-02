from pydantic import BaseModel

# USER
class CreateUser(BaseModel):
    email: str
    password: str

class GetUser(BaseModel):
    id: int
    email: str

class UpdateUser(BaseModel):
    email: str

# Image
class CreateImage(BaseModel):
    name: str
    location: str

class GetImage(BaseModel):
    id: int
    name: str
    location: str