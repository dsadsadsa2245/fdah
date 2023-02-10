
from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str
    password: str


class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
