#!/usr/bin/python3
"""
FileStorage class file
"""
from models.base_model import BaseModel
import json
import models


class FileStorage():
    """class that serializes\deserialize instances to a JSON """

    path = "file.json"
    __file_path = path
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""

        if obj is not None:
            keyx = obj.__class__.__name__ + "." + obj.id
            self.__objects[keyx] = obj

    def save(self):
        """serializes objects to the JSON file"""

        json_objects = {}

        for ob in self.__objects.keys():
            json_objects[ob] = self.__objects[ob].to_dict()

        with open(self.__file_path, 'w') as filex:
            json.dump(json_objects, filex)

    def reload(self):
        """ reload the saved instances"""

        try:
            with open(self.__file_path, 'r') as fx:
                lo = json.load(fx)
            for x in lo.keys():
                self.__objects[x] = BaseModel(**lo[x])

        except FileNotFoundError:
            pass
