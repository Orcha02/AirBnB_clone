#!/usr/bin/python3
"""New testing module"""


import unittest
from models.base_model import BaseModel
from models.user import User
import os


class TestMyUser(unittest.TestCase):
    """Class TestMyUser to test class User"""

    def setUp(self):
        """setting up each test"""
        self.new = User()
        self.base = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """cleaning up after each test"""
        del self.new
        del self.base
        del self.base2

    def test_empty_strings_before(self):
        """Check if the strings are empty before assignment"""
        self.assertFalse(self.new.email)
        self.assertFalse(self.new.password)
        self.assertFalse(self.new.first_name)
        self.assertFalse(self.new.last_name)

    def test_methods_exist(self):
        """Check if the methods are present"""
        assert self.new.__init__ is not None
        assert self.new.save is not None
        assert self.new.to_dict is not None
        assert self.new.updated_at is not None
        assert self.new.__str__ is not None

    def test_attributes_exist(self):
        """Assign attributes and check if they are not None"""
        self.new.email = 'James.grijalba@holberton.com'
        self.new.password = 'imsupercool'
        self.new.first_name = 'Frank'
        self.new.last_name = 'Grijalba'

        self.assertNotEqual(self.new.email, None)
        self.assertNotEqual(self.new.password, None)
        self.assertNotEqual(self.new.first_name, None)
        self.assertNotEqual(self.new.last_name, None)

    def test_attributes_are_correct(self):
        """Check if assigments happened as intended"""
        self.new.email = 'James.grijalba@holberton.com'
        self.new.password = 'imsupercool'
        self.new.first_name = 'Frank'
        self.new.last_name = 'Grijalba'

        self.assertEqual(self.new.email, 'James.grijalba@holberton.com')
        self.assertEqual(self.new.password, 'imsupercool')
        self.assertEqual(self.new.first_name, 'Frank')
        self.assertEqual(self.new.last_name, 'Grijalba')

    def test_if_str(self):
        """Check if the attributes are strings"""
        self.new.email = 'James.grijalba@holberton.com'
        self.new.password = 'imsupercool'
        self.new.first_name = 'Frank'
        self.new.last_name = 'Grijalba'

        self.assertTrue(type(self.new.email) == str)
        self.assertTrue(type(self.new.password) == str)
        self.assertTrue(type(self.new.first_name) == str)
        self.assertTrue(type(self.new.last_name) == str)

if __name__ == '__main__':
    unittest.main()
