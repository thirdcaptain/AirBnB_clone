#!/usr/bin/python3
"""creating a file storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """a new class that serializes instances to a JSON file and back"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all objects from the storage"""
        return FileStorage.__objects

    def new(self, obj):
        """set the objects in the storage in a specific order"""
        key = "{}.{}".format(str(type(obj).__name__), obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """saves the changes to a json file"""
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """get the instance from a JSON file"""
        load_dict = {}
        try:
            with open(self.__file_path, "r") as f:
                load_dict = json.load(f)
                for key, value in load_dict.items():
                    obj = eval(value['__class__'])(**value)
                    FileStorage.__objects[key] = obj
        except:
            pass
