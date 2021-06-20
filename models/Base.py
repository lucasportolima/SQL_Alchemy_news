from sqlalchemy import (
    Column,
    Integer
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declared_attr


class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)
