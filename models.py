
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100))

    @property
    def serialize(self):
        # Returns object data in easily serializeable format
        return {
           'id': self.id,
           'name': self.name,
           'emai': self.email
        }


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    @property
    def serialize(self):
        return {
           'id': self.id,
           'name': self.name
        }


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(1000))
    updated = Column(DateTime, default=datetime.datetime.utcnow)
    categories_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship(Categories)

    @property
    def serialize(self):
        # Returns object data in easily serializeable format
        return {
           'id': self.id,
           'title': self.title,
           'description': self.description,
           'updated': self.updated
        }

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
