#!/usr/bin/python3
"""Test module"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """New class to test class BaseModel"""

    def setUp(self):
        """Setting up"""
        self.my_BaseModel = BaseModel()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.my_BaseModel

    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.my_BaseModel, BaseModel)

    def test_id(self):
        """Test if the id of two instances are different"""
        my_BaseModel2 = BaseModel()
        self.assertNotEqual(self.my_BaseModel.id, my_BaseModel2.id)
