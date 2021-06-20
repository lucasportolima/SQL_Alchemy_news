from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

from .Base import Base


class Person(Base):
    __tablename__ = 'person'

    name = Column(String)
    email = Column(String)
    posts = relationship('Post', backref='person')

    def __init__(self, field):
        for key, value in field.items():
            setattr(self, key, value)

    def __repr__(self):
        return f'Person({self.name})'
