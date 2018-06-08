#!/usr/bin/python3
"""create a class that defines all common attributes/methods for others"""
import uuid
from datetime import datetime
import dateutil.parser


class BaseModel:
    """writing a base class"""

    def __init__(self, id=None):
        """constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = dateutil.parser.parse(created_at)
        self.updated_at = dateutil.parser.parse(updated_at)

    def __str__(self):
        """returns a readable string"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """updates updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
