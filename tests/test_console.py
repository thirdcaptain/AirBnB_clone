#!/usr/bin/python3
"""tests console
"""


from console import HBNBCommand
import sys
import unittest
from unittest.mock import create_autospec

class Test_Console(unittest.TestCase):
    """console unittest
    """

    def test_quit(self):
        """tests quit command
        """
        name = self.create()
        self.assertTrue(name.onecmd("quit"))
