import json

from importlib import import_module
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    def __init__(self, file_path='file.json'):
        self.file_path = file_path
        self.objects = {}

    def all(self, cls=None):
        if cls is None:
            return self.objects
        return {k: v for k, v in self.objects.items() if isinstance(v, cls)}

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.objects[key] = obj

    def save(self):
        data = {k: v.to_dict() for k, v in self.objects.items()}
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.objects = self.deserialize_objects(data)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.objects.pop(key, None)

    def deserialize_objects(self, data):
        classes = self.get_model_classes()
        objects = {}
        for key, val in data.items():
            class_name = val['__class__']
            if class_name in classes:
                cls = classes[class_name]
                objects[key] = cls(**val)
        return objects

    def get_model_classes(self):
        model_modules = [
            'models.base_model',
            'models.user',
            'models.place',
            'models.state',
            'models.city',
            'models.amenity',
            'models.review'
        ]
        classes = {}
        for module_name in model_modules:
            module = import_module(module_name)
            for name, obj in module.__dict__.items():
                if isinstance(obj, type) and issubclass(obj, BaseModel):
                    classes[obj.__name__] = obj
        return classes


# #!/usr/bin/python3
# """This module defines a class to manage file storage for hbnb clone"""
# import json


# class FileStorage:
#     """This class manages storage of hbnb models in JSON format"""
#     __file_path = 'file.json'
#     __objects = {}

#     def all(self, cls=None):
#         """Returns a dictionary of models currently in storage"""
#         return FileStorage.__objects

#     def new(self, obj):
#         """Adds new object to storage dictionary"""
#         self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

#     def save(self):
#         """Saves storage dictionary to file"""
#         with open(FileStorage.__file_path, 'w') as f:
#             temp = {}
#             temp.update(FileStorage.__objects)
#             for key, val in temp.items():
#                 temp[key] = val.to_dict()
#             json.dump(temp, f)

#     def reload(self):
#         """Loads storage dictionary from file"""
#         from models.base_model import BaseModel
#         from models.user import User
#         from models.place import Place
#         from models.state import State
#         from models.city import City
#         from models.amenity import Amenity
#         from models.review import Review

#         classes = {
#                     'BaseModel': BaseModel, 'User': User, 'Place': Place,
#                     'State': State, 'City': City, 'Amenity': Amenity,
#                     'Review': Review
#                   }
#         try:
#             temp = {}
#             with open(FileStorage.__file_path, 'r') as f:
#                 temp = json.load(f)
#                 for key, val in temp.items():
#                     self.all()[key] = classes[val['__class__']](**val)
#         except FileNotFoundError:
#             pass

#     def delete(self, obj=None):
#         """ delete an existing element
#         """
#         if obj:
#             key = "{}.{}".format(type(obj).__name__, obj.id)
#             del self.__objects[key]
