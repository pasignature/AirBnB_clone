#!/usr/bin/python3
"""Defines unittests for models/place.py.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """testing instantiation of the Place class."""

    def test_instantiation(self):
        self.assertEqual(Place, type(Place()))
