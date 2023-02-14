from sqlalchemy import Column, String, Integer

from models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    username = Column(String(50), unique=True)
    password = Column(String, nullable=False)
    gmail = Column(String, nullable=True)
    number = Column(String)


class Planets(BaseModel):
    __tablename__ = 'PLanet'
    name = Column(String(30), unique=True)
    number = Column(String, nullable=False)
    type=Column(String, nuiiable)
    size_height = Column(Integer)
    size_width = Column(Integer)
    size_lenght = Column(Integer)
    access_key = Column(String, nullable=False)

# alembic revision --autogenerate -m "Comment"
# alembic upgrade head
#
