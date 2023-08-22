#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import shlex


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of __objects"""
        ob_dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    ob_dic[key] = self.__objects[key]
            return (ob_dic)
        else:
            return self.__objects

    def new(self, obj):
        """sets in dict __objects the obj with key <obj class name>.id """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp_dict = {}
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            # temp.update(FileStorage.__objects)
            for key, val in self.__objects.items():
                temp_dict[key] = val.to_dict()
            json.dump(temp_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    val = eval(val["__class__"])(**val)
                    self.__objects[key] = val
                    # self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ calls reload()
        """
        self.reload()
