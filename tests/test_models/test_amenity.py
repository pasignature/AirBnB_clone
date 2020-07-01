#!/usr/bin/python3
"""Defines unittests for models/amenity.py
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_instantiation(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_attribute(self):
        self.assertIsInstance(Amenity.name, str)

if __name__ == "__main__":
    unittest.main()
