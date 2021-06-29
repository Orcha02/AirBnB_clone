#!/usr/bin/python3
"""New testing module"""


import pep8
import unittest
from models.base_model import BaseModel
from models.user import User


class TestMyUser(unittest.TestCase):
    """Class TestMyUser to test class User"""

    def setUp(self):
        """setting up each test"""
        self.my_user = User()
        self.base = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """cleaning up after each test"""
        del self.my_user
        del self.base
        del self.base2

    def test_empty_strings_before(self):
        """Check if the strings are empty before assignment"""
        self.assertFalse(self.my_user.email)
        self.assertFalse(self.my_user.password)
        self.assertFalse(self.my_user.first_name)
        self.assertFalse(self.my_user.last_name)

    def test_methods_exist(self):
        """Check if the methods are present"""
        assert self.my_user.__init__ is not None
        assert self.my_user.save is not None
        assert self.my_user.to_dict is not None
        assert self.my_user.updated_at is not None
        assert self.my_user.__str__ is not None

    def test_attributes_exist(self):
        """Assign attributes and check if they are not None"""
        self.my_user.email = 'James.grijalba@holberton.com'
        self.my_user.password = 'imsupercool'
        self.my_user.first_name = 'Frank'
        self.my_user.last_name = 'Grijalba'

        self.assertNotEqual(self.my_user.email, None)
        self.assertNotEqual(self.my_user.password, None)
        self.assertNotEqual(self.my_user.first_name, None)
        self.assertNotEqual(self.my_user.last_name, None)

    def test_attributes_are_correct(self):
        """Check if assigments happened as intended"""
        self.my_user.email = 'James.grijalba@holberton.com'
        self.my_user.password = 'imsupercool'
        self.my_user.first_name = 'Frank'
        self.my_user.last_name = 'Grijalba'

        self.assertEqual(self.my_user.email, 'James.grijalba@holberton.com')
        self.assertEqual(self.my_user.password, 'imsupercool')
        self.assertEqual(self.my_user.first_name, 'Frank')
        self.assertEqual(self.my_user.last_name, 'Grijalba')

    def test_if_str(self):
        """Check if the attributes are strings"""
        self.my_user.email = 'James.grijalba@holberton.com'
        self.my_user.password = 'imsupercool'
        self.my_user.first_name = 'Frank'
        self.my_user.last_name = 'Grijalba'

        self.assertTrue(type(self.my_user.email) == str)
        self.assertTrue(type(self.my_user.password) == str)
        self.assertTrue(type(self.my_user.first_name) == str)
        self.assertTrue(type(self.my_user.last_name) == str)

    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.my_user, User)


class TestCodeFormat(unittest.TestCase):
    """Class to do pep8 validation."""
    def test_pep8(self):
        """Test that we conform to pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = pep8style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

if __name__ == '__main__':
    unittest.main()
