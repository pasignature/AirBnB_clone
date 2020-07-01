#!/usr/bin/python3
"""
Contains the TestFileStorageDocs classes
"""

from datetime import datetime
import inspect
from models.engine import file_storage
from models.base_model import BaseModel
from models.user import User
import json
import os
import pep8
import unittest
FileStorage = file_storage.FileStorage
classes = {"BaseModel": BaseModel, "User": User}


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)


 
