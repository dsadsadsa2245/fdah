from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    username: str
    password: str

    def split(self):
        return True


class UserCreateSchema(UserBaseSchema):
    pass


class UserAuthSchema(UserBaseSchema):
    pass


class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


