#!/usr/bin/python3
"""
FileStorage class file
"""
from models.base_model import BaseModel
from models.user import User
import json
import models


class FileStorage():
    """class that serializes\deserialize instances to a JSON """

    path = "file.json"
    __file_path = path
    __objects = {}
    kryptix = ''
    cll = [BaseModel, User]
    strx = ['BaseModel', 'User']

    def all(self):
        """returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""

        if obj is not None:
            keyx = obj.__class__.__name__ + "." + obj.id
            self.__objects[keyx] = obj
            FileStorage.kryptix = obj.__class__.__name__

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
                #if x.split('.')[0] in FileStorage.strx:
                self.__objects[x] = FileStorage.cll[FileStorage.strx.index(x.split('.')[0])](**lo[x])

        except FileNotFoundError:
            pass
