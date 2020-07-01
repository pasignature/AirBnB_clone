#!/usr/bin/python3
"""
User class test
"""

from datetime import datetime
import inspect
from models import user
from models.base_model import BaseModel
import pep8
import unittest
User = user.User


class TestUser(unittest.TestCase):
    """User class Test"""
    def test_is_subclass(self):
        """Test User class instnatiation"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
