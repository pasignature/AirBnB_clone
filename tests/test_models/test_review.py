#!/usr/bin/python3
"""Defines unittests for models/review.py.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """testing classinstantiation the class."""

    def test_subclass(self):
        self.assertEqual(Review, type(Review()))

    def test_ids_generation(self):
        instance1 = Review()
        instance2 = Review()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_attribute_object_time(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_attribute2_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

if __name__ == "__main__":
    unittest.main()
