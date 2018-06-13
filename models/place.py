#!/usr/bin/python3
"""defines place class
"""

from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class Place(BaseModel):
    """public place attributes
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
