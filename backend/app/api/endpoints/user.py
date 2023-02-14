from typing import List

import sqlalchemy
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.dialects.postgresql import psycopg2
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.responses import Response

from db.init_db import get_db
from models.user import User
from schemas.user import UserRead, UserCreateSchema, UserAuthSchema, UserList, TokenAccess, StarShips
from passlib.context import CryptContext

from security.deps import create_access_token

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"])
ALGORITHM = "HS256"


@router.post('/users', response_model=UserRead)
def users_get(

        user_in: UserCreateSchema,
        db: Session = Depends(get_db),  # коннект с базой данных, depends - если depends не работает,весь оставшийся код не будет работать в границах этой функции
):
    user_dict = user_in.dict()
    # переводит в диктионари
    user_dict['password'] = pwd_context.hash(user_dict['password'])
    user = User(**user_dict)
    db.add(user) #add все собирает в одну кучу, а камит отправляет кучу на базу данных

    try:
        db.commit()   # отправляет в базу данных,обновление
    except IntegrityError:
        raise HTTPException(400, detail="lalal")  # используй вместо:  return Response(content="user_not_found lalala", status_code=404)
    return user


@router.post('/autorisation', response_model=TokenAccess) #respose_model возвращает в результат апишки
def autorisation(
        user_name: UserAuthSchema,
        database: Session = Depends(get_db),
):
    getted = database.query(User).filter(User.username == user_name.username).all()  # query вытаскивает как select
    getted = getted[0] if len(getted) == 1 else None
    if getted is None:
        return Response(content="user_not_found lalala", status_code=404)
    if pwd_context.verify(user_name.password, getted.password) is False:  # verify это проверить
        return Response(content="user_not_found lalala", status_code=400)
    token = create_access_token(getted.id)

    return {"user": getted, "token": token}


@router.get("/all_users", response_model=List[UserRead])
def api_list( db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get("/search_id",response_model=UserList)
def search_user(id: int, db: Session = Depends(get_db)):   #somethind: parametr - это вызовет строку принимающуя указанные данные
    getted = db.query(User).get(id)
    return getted





# @router.get("/starships",response_model=StarShips)
# def search_starship(name:str, db:Session=Depends(get_db)):
#     a=db.query(StarShips)