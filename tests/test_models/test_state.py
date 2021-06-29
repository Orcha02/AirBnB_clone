#!/usr/bin/python3
"""Test module"""


import unittest
from models.state import State


class TestMyState(unittest.TestCase):
    """New class to test class State"""

    def setUp(self):
        """Setting up"""
        self.my_state = State()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.my_state

    def test_is_instance(self):
        """Check if an instance belongs to class State"""
        self.assertIsInstance(self.my_state, State)

    def test_if_str(self):
        """Check if the attribute is str"""
        self.assertIsInstance(self.my_state.name, str)

    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.my_state, State)

if __name__ == '__main__':
    unittest.main()
