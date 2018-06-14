#!/usr/bin/python3
import pep8
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.city import City
import sys
import models
import unittest
import json
import os
import datetime


class TestFileStorageMethods(unittest.TestCase):
    """class with tests"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def setUp(self):
        """setting up"""
        pass

    def tearDown(self):
        """cleaning after"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_doc(self):
        """testing docstrings"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all(self):
        """test method all"""
        my_model = FileStorage()
        my_model_dict = my_model.all()
        self.assertIsNotNone(my_model_dict)
        self.assertEqual(type(my_model_dict), dict)
        self.assertIs(my_model_dict, my_model._FileStorage__objects)

    def test_new(self):

        my_model = FileStorage()
        my_model_dict = my_model.all()
        isaac = User()
        isaac.id = 666
        isaac.name = "Leviathan"
        my_model.new(isaac)
        key = "{}.{}".format(isaac.__class__.__name__, isaac.id)
        self.assertIsNotNone(my_model_dict[key])

    def test_reload(self):

        my_model = FileStorage()
        with open("file.json", "w") as f:
            f.write("{isaaac}")
        with open("file.json", "r") as s:
            for line in s:
                self.assertEqual(line, "{isaaac}")
        self.assertIs(my_model.reload(), None)
