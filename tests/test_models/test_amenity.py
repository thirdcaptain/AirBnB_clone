#!/usr/bin/python3
"""tests amenity class
"""

from models.amenity import Amenity
import pep8
import os
import unittest

class TestAmenity(unittest.TestCase):
    """tests Amenity"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstrings(self):
        """testing docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_hasattribute(self):
        my_model = Amenity()
        self.assertTrue(hasattr(my_model, "__init__"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "id"))
