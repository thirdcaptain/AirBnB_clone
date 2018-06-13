#!/usr/bin/python3
"""defines review class
"""

from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


class Review(BaseModel):
    """public review attributes
    """
    place_id = ""
    user_id = ""
    text = ""
