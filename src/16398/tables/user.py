from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    name = Column(String, primary_key=True)
    family = Column(String, primary_key=True)
    likes = Column(Integer)

    order_fields = ['name', 'family']

    def to_json(self):
        return {
            'name': self.name,
            'family': self.family,
            'likes': self.likes
        }
