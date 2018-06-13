#!/usr/bin/python3
import pep8
from models.base_model import BaseModel
import unittest
import json
import os
import datetime


class TestBaseModelMethods(unittest.TestCase):
    """class with tests"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def setUp(self):
        """setting up"""
        pass

    def tearDown(self):
        """cleaning after"""
        try:
            del file.json
        except:
            pass

    def test_doc(self):
        """testing docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_to_dict(self):
        """checking classes of the dict"""

        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        my_model_json = my_model.to_dict()
        for key in my_model_json:
            self.assertNotIsInstance(my_model_json[key], datetime.datetime)

    def test_save(self):
        """check if it saves changes"""

        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(os.path.isfile('file.json'))
