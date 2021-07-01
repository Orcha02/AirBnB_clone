#!/usr/bin/python3
"""Test module"""


import pep8
import unittest
from models.base_model import BaseModel
import datetime


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

    def test_dict_class(self):
        """Checks if the key __class__ exists"""
        self.assertEqual("BaseModel",
                         (self.my_BaseModel.to_dict())["__class__"])

    def test_type_created_at(self):
        """Test that the new_model's updated_at data type is datetime"""
        BaseModel_to_dict = self.my_BaseModel.to_dict()
        new_model = BaseModel(BaseModel_to_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))

    def test_type_updated_at(self):
        """Test that the new_model's created_at data type is datetime"""
        BaseModel_to_dict = self.my_BaseModel.to_dict()
        new_model = BaseModel(BaseModel_to_dict)
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

    def test_id_type(self):
        """Checks if id is of type string"""
        self.assertEqual("<class 'str'>", str(type(self.my_BaseModel.id)))

    def test_save(self):
        """
        Check if the attribute updated_at (date) is updated for
        the same object with the current date
        """
        first_updated = self.my_BaseModel.updated_at
        self.my_BaseModel.save()
        second_updated = self.my_BaseModel.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_kwargs(self):
        """Check that has kwargs as attributes values."""
        self.my_BaseModel.name = "Holberton"
        self.my_BaseModel.my_number = 89
        json_attributes = self.my_BaseModel.to_dict()

        my_BaseModel2 = BaseModel(**json_attributes)

        self.assertIsInstance(my_BaseModel2, BaseModel)
        self.assertIsInstance(json_attributes, dict)
        self.assertIsNot(self.my_BaseModel, my_BaseModel2)


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
