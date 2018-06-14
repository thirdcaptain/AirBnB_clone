#!/usr/bin/python3

import pep8
from models.engine.file_storage import FileStorage
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
            del file.json
        except:
            pass

    def test_doc(self):
        """testing docstrings"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_save(self):
        """check if it saves changes"""
        my_model = FileStorage()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(os.path.isfile('file.json'))
