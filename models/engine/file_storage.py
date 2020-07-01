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
    """
    ------------------
    CLASS: FileStorage
    ------------------
    """

    # ------------------------------- #
    #       PUBLIC ATTRIBUTES         #
    # ------------------------------- #

    #path to the Json file
    __file_path = 'file.json'
    #objects dictionary where to save
    __objects = {}

    kryptix = ''
    cll = [BaseModel, User]
    strx = ['BaseModel', 'User']

    def all(self):
        """
        ---------------------------
        PUBLIC INSTANCE METHOD: ALL
        ---------------------------
        DESCRIPTION:
            Returns the dictionary stored in
            the attribute '__objects'
        ARGS:
            @self: current instance
        """

        return self.__objects

    def new(self, obj):
        """
        ---------------------------
        PUBLIC INSTANCE METHOD: NEW
        ---------------------------
        DESCRIPTION:
            Adds the necessary objects to the
            '__objects' attribute
        ARGS:
            @self: current instance
            @obj: object to add to '__objects'
        """

        if obj is not None:
            keyx = obj.__class__.__name__ + "." + obj.id
            self.__objects[keyx] = obj
            FileStorage.kryptix = obj.__class__.__name__

    def save(self):
        """
        ----------------------------
        PUBLIC INSTANCE METHOD: SAVE
        ----------------------------
        DESCRIPTION:
            Serializes items in __objects to JSON
            and dumps the output into a file defined
            by '__file_path'
        ARGS:
            @self: current instance
        """

        json_objects = {}

        for ob in self.__objects:
            json_objects[ob] = self.__objects[ob].to_dict()

        with open(self.__file_path, 'w') as filex:
            json.dump(json_objects, filex)

    def reload(self):
        """
        ------------------------------
        PUBLIC INSTANCE METHOD: RELOAD
        ------------------------------
        DESCRIPTION:
            Deserializes a JSON file, loads up
            and loads up all of the instances
            found in the file into the attribute
            '__objects'
        """

        try:
            with open(self.__file_path, 'r') as fx:
                d = json.load(fx)

            for x in d.keys():
                #self.__objects[x] = classes[d[x]["__class__"]](**d[x])
                self.__objects[x] = FileStorage.cll[FileStorage.strx.index(x.split('.')[0])](**lo[x])y

        except FileNotFoundError:
            pass
