#!/usr/bin/python3

"""
Database Storage module
"""
from sqlalchemy import Column, Table
import os
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City
from models.base_model import BaseModel, Base


class DBStorage:
    """ DataBase Storage class """
    __engine = None
    __session = None

    def __init__(self):
        """ Time to make some shit """
        from sqlalchemy import create_engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                        os.getenv('HBNB_MYSQL_USER'),
                        os.getenv('HBNB_MYSQL_PWD'),
                        os.getenv('HBNB_MYSQL_HOST'),
                        os.getenv('HBNB_MYSQL_DB'), pool_pre_ping=True))
        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Doing all of something """
        types = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
            }
        if cls is not None and cls != "":
            the_type = types.get(cls)
            result = self.__session.query(the_type).all()
        else:
            result = self.__session.query(State).all()
            result = result + self.__session.query(City).all()
            result = result + self.__session.query(User).all()
            result = result + self.__session.query(Place).all()
            result = result + self.__session.query(Review).all()
            result = result + self.__session.query(Amenity).all()
        return_dict = {}
        for item in result:
            key = item.__class__.__name__ + "." + item.id
            value = item
            return_dict.update({key: value})
        return return_dict

    def new(self, obj):
        """ Adds a new object to the database """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """ Saves the new stuff or whatever idk I'm drunk """
        self.__session.commit()

    def delete(self, obj):
        """ Deletes the object from DB Cooper """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Lock and reload """
        from sqlalchemy.orm import sessionmaker, scoped_session
        Base.metadata.create_all(self.__engine)
        sesh_thing = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh_thing)
        self.__session = Session()

    def close(self):
        """ Docstring for close method """
        self.__session.close()
