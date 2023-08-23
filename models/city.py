#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from models import storage_type


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    if storage_type == 'db':

        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        # places = relationship('Place', cascade='all, delete, delete-orphan',
        #                       backref='cities')
    else:
        state_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
