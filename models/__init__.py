#!/usr/bin/python3
"""This module instantiates a storage object"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
