from sqlalchemy import Column, String, Integer

from models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    username = Column(String(50), unique=True)
    password = Column(String, nullable=True)

