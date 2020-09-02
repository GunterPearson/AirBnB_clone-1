#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, DateTime, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """ getter attriute for cities"""
            from models import storage
            from models.city import City
            c_list = []
            for c in list(storage.all(City).values()):
                if c.state_id == self.id:
                    c_list.append(c)
            return c_list
