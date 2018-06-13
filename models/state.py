#!/usr/bin/python3
"""defines state class
"""

from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class State(BaseModel):
    """public attributes
    """
    name = ""
