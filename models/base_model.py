#!/usr/bin/python3
"""create a class that defines all common attributes/methods for others"""
import uuid
from datetime import datetime
import storage


class BaseModel:
    """writing a base class"""

    def __init__(self, *args, **kwargs):
        """constructor"""
        list = ["id", "created_at"]
        if kwargs:
            for key, value in kwargs.items():
                if key in list:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            storage.new(self)
        self.updated_at = datetime.now()

    def __str__(self):
        """returns a readable string"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """updates updated_at"""
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return {__class__.__name__.id: self.__dict__}
