#!/usr/bin/python3
"""
FileStorage class file
"""
from models.base_model import BaseModel
from models.user import User
import json
import models

classes = {"BaseModel": BaseModel, "User": User}


class FileStorage():
    """class that serializes\deserialize instances to a JSON """

    __file_path = 'file.json'
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

        for ob in self.__objects:
            json_objects[ob] = self.__objects[ob].to_dict()

        with open(self.__file_path, 'w') as filex:
            json.dump(json_objects, filex)

    def reload(self):
        """ reload the saved instances"""

        try:
            with open(self.__file_path, 'r') as fx:
                d = json.load(fx)

            for x in d:
                self.__objects[x] = classes[d[x]["__class__"]](**d[x])

        except FileNotFoundError:
            pass
