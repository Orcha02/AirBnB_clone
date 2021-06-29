#!/usr/bin/python3
"""Test module"""


import pep8
import unittest
from models.city import City


class TestMyCity(unittest.TestCase):
    """New class to test class City"""

    def setUp(self):
        """Setting up"""
        self.my_city = City()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.my_city

    def test_is_instance(self):
        """Check if new instance belongs to class City"""
        self.assertTrue(type(self.my_city) is City)

    def test_id(self):
        """Check if state_id is a string"""
        self.assertTrue(type(self.my_city.state_id) is str)

    def test_name(self):
        """Check if name is a str"""
        self.assertTrue(type(self.my_city.name) is str)

    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.my_city, City)

    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(self.my_city.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)


class TestCodeFormat(unittest.TestCase):
    """Class to do pep8 validation."""
    def test_pep8(self):
        """Test that we conform to pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        file1 = 'models/city.py'
        file2 = 'tests/test_models/test_city.py'
        result = pep8style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

if __name__ == '__main__':
    unittest.main()
