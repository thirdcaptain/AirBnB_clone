#!/usr/bin/python3
"""defines city class
"""

from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class City(BaseModel):
    """public city attributes
    """
    state_id = ""
    name = ""
