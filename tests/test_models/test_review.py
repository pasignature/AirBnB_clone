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

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))
