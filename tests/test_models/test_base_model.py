#!/usr/bin/python3
"""Test module"""


import pep8
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

    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(self.my_BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


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
