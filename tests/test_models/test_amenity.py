#!/usr/bin/python3
"""Test module"""


import unittest
from models.amenity import Amenity


class TestMyAmenity(unittest.TestCase):
    """New class to test class Amenity"""

    def setUp(self):
        """Setting up"""
        self.my_amenity = Amenity()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.my_amenity

    def test_is_instance(self):
        """Check if attributes are of a correct type"""
        self.assertIsInstance(self.my_amenity, Amenity)

    def test_if_str(self):
        """Check if the attribute is str"""
        self.assertIsInstance(self.my_amenity.name, str)

    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.my_amenity, Amenity)

if __name__ == '__main__':
    unittest.main()
