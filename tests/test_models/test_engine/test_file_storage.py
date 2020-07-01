#!/usr/bin/python3
"""
Contains the TestFileStorageDocs classes
"""

from datetime import datetime
import inspect
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import json
import os
import pep8
import unittest
#FileStorage = file_storage.FileStorage
classes = {"BaseModel": BaseModel, "User": User}


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """"""
        self.engine = FileStorage()
        self.ob = BaseModel()
        #self.engine.new(self.ob)
        #self.key = self.ob.__class__.__name__ + '.' + self.obj.id

    def test_no_arg(self):
        self.assertIsNone(self.engine.new(self.ob))
   
    def test_all(self):
        self.assertEqual(dict, type(self.engine.all()))

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
