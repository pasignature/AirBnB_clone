#!/usr/bin/python3
""" Unittest for Holberton HBnB BaseModel class """
import unittest
import datetime
import uuid
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Tests the BaseModel class's methods and attributes. """

    def setUp(self):
        """ sets kwargs properly """
        try:
            os.remove("file.json")
        except:
            pass
        self.base1 = BaseModel(number=89,
                               created_at="2020-06-28T01:25:18.335269",
                               updated_at="2020-06-28T01:25:18.335279",
                               id="0e6ad280-ebf5-4bc8-0671-2a0e8daff35d")
        self.base2 = BaseModel()
        self.base3 = BaseModel()

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

def test_init_with_insufficient_args(self):
        with self.assertRaises(Exception):
            base0 = BaseModel(number=89)

    def test_init_with_sufficient_args(self):
        self.assertEqual(self.base1.number, 89)
        self.assertEqual(self.base1.created_at,
                         datetime.datetime(2020, 06, 28T01, 25, 18, 335269))
        self.assertEqual(self.base1.updated_at,
                         datetime.datetime(2020, 06, 28T01, 25, 18, 335279))
