#!/usr/bin/python3
"""defines amenity class
"""

from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


class Amenity(BaseModel):
    """public amenity attributes
    """
    name = ""
