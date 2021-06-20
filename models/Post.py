from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)

from .Base import Base


class Post(Base):
    __tablename__ = 'post'

    title = Column(String)
    content = Column(String)
    autor_id = Column(Integer, ForeignKey('person.id'))

    def __init__(self, field):
        for key, value in field.items():
            setattr(self, key, value)

    def __repr__(self):
        return f'Post({self.title})'
