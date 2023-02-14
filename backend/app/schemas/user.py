from typing import Optional

from pydantic import BaseModel


class UserBaseSchema(BaseModel):  # BaseModel-без него схема не работает
    username: str
    gmail: Optional[str]
    number: Optional[str]  # optinal- делает необязательным данные значения


class UserCreateSchema(UserBaseSchema):
    password: str


class UserAuthSchema(BaseModel):
    username: str
    password: str


class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class TokenAccess(BaseModel):
    user: UserRead
    token: str


class UserList(UserBaseSchema):
    id: int

    class Config:
        orm_mode = True  # отрывок кода для вписывания id


class StarShips(BaseModel):
    name: str
    number: str
    model: str
    size_height: int
    size_width: int
    size_lenght: int
    access_key: str
