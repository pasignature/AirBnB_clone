#!/usr/bin/python3
"""Defines unittests for models/state.py.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing the State class instantiation"""

    def test_class_instantiation(self):
        self.assertEqual(State, type(State()))

if __name__ == "__main__":
    unittest.main()
