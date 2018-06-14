#!/usr/bin/python3
"""unit test for BaseModel class
"""
import pep8
from models.base_model import BaseModel
import unittest
import json
import os


class TestBaseModelMethods(unittest.TestCase):
    """class with tests"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

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
        my_model_json = my_model.to_dict()
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertEqual(my_model.__class__.__name__, 'BaseModel')

    def test_save(self):
        """check if it saves changes"""

        my_model = BaseModel()
        my_model.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_hasattribute(self):
        """check attributes of BaseModel
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "__init__"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "id"))

    def test_init(self):
        """tests initialization"""
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model, BaseModel))

if __name__ == "__main__":
    unittest.main()
