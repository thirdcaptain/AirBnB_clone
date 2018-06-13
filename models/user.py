#!/usr/bin/python3
"""model defines User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User public attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
