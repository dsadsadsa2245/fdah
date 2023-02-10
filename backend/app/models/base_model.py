from sqlalchemy import Column, Integer

from db.init_db import Base


class BaseModel(Base):
    __abstract__ = True
    __tablename__ = None
    id = Column(Integer, primary_key=True, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__tablename__ = self.__class__.__name__
