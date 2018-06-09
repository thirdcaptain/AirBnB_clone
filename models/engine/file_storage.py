#!/usr/bin/python3
"""creating a file storage"""
import json
from models.base_model import BaseModel

class FileStorage:
    """a new class that serializes instances to a JSON file and back"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        """constructor"""
        pass

    def all(self):
        """"""
        return FileStorage.__objects

    def new(self, obj):
        """"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """"""
        new_dict = {}
        for key, obj in self.__objects.items():
            new_dict[key] = obj
        with open(self.__file_path, "a") as f:
            json.dumps(new_dict, f)

    def reload(self):
        """"""
        load_dict = {}
        try:
            with open(self.__file_path, "r") as f:
                load_dict = json.load(f)
                for key, value in load_dict.items():
                    obj = BaseModel(**value)
                    self.__object[key] = obj
        except:
            pass
        #       if os.path.isfile(type(self).__file_path):
