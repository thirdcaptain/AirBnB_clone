#!/usr/bin/python3
"""tests console
"""
from console import HBNBCommand
import sys
import unittest
from unittest.mock import create_autospec


class TestConsole(unittest.TestCase):
    """console unittest
    """
    def setUp(self):
        """seting up IO"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self):
        """a helper method to build an instance"""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_quit(self):
        """tests quit command
        """
        name = self.create()
        self.assertTrue(name.onecmd("quit"))

if __name__ == "__main__":
    unittest.main()
