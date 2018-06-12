#!/usr/bin/python3
"""create a class that defines all common attributes/methods for others"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """writing a base class"""

    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['updated_at', 'created_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if "__class__" not in key:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns a readable string"""
        return "[{}] ({}) {}".format(
            str(type(self).__name__), self.id, str(self.__dict__))

    def save(self):
        """updates updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""

        new_dict = {}
        new_dict.update(self.__dict__)
        new_dict['__class__'] = str(type(self).__name__)
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
