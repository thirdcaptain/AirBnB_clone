#!/usr/bin/python3
"""tests city class
"""

from models.city import City
import pep8
import os
import unittest

class TestCity(unittest.TestCase):
    """tests City"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstrings(self):
        """testing docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_hasattribute(self):
        my_model = City()
        self.assertTrue(hasattr(my_model, "__init__"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "id"))
