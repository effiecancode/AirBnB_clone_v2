#!/usr/bin/python3
"""New Database Engine"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage():
    """file storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query current db session of all objs like in filestorage
        If cls is None, queries all types of objects.
        return: dict of queried classes key:val = <class name>.<obj id> = obj
        """

        all_classes = (Amenity, City, Place, Review, State, User)
        objects = dict()

        if cls is None:
            for item in all_classes:
                query = self.__session.query(item)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.name__, obj.id)
                    objects[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj
        return objects

    def new(self, obj):
        """ add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all the changes to current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all the tables in database and initialize a new session"""
        Base.metadata.create_all(self.__engine)

        my_session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        my_actual_session = scoped_session(my_session)
        self.__session = my_actual_session()

    def close(self):
        """close the working SQLalchemy session"""
        self.__session.close()
