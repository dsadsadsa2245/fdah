from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.init_db import get_db
from models.user import User
from schemas.user import UserRead, UserCreateSchema
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"])
ALGORITHM = "HS256"


@router.post('/users', response_model=UserRead)
def users_get(
        user_in: UserCreateSchema,
        db: Session = Depends(get_db),
):
    user_dict = user_in.dict()
    user_dict['password'] = pwd_context.hash(user_dict['password'])
    user = User(**user_dict)
    db.add(user)
    db.commit()

    return user
# @router.post('/autorisation',response_model=UserRead)
# def autorisation()