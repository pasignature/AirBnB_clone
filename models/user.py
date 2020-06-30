#!/usr/bin/python3
"""
a class User that inherits from BaseModel:
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """a class User that inherits from BaseModel"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """a class constructor"""

        super().__init__(*args, **kwargs)
        models.storage.new(self)
        models.storage.save()
