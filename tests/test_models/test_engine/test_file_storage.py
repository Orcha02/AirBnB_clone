#!/usr/bin/python3
"""Test module"""


import pep8
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """New class to test class Amenity"""

    def setUp(self):
        """Setting up"""
        self.my_file_storage = FileStorage()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.my_file_storage

    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.my_file_storage, FileStorage)

    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(self.my_file_storage.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)

    def test_path_type(self):
        """Check if path is of type string"""
        self.assertIsInstance(self.engine._FileStorage__file_path, str)

    def test_objects(self):
        """Check __objects attribute"""
        self.assertEqual(dict, type(my_file_storage.all()))

    def tests(self):
        """Check if functions are defined."""
        self.assertTrue(hasattr(self.my_file_storage, 'new'))
        self.assertTrue(hasattr(self.my_file_storage, 'reload'))
        self.assertTrue(hasattr(self.my_file_storage, 'save'))
        self.assertTrue(hasattr(self.my_file_storage, 'all'))

    def test_all(self):
        """Check the all"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)

class TestCodeFormat(unittest.TestCase):
    """Class to do pep8 validation."""
    def test_pep8(self):
        """Test that we conform to pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        file1 = 'models/amenity.py'
        file2 = 'tests/test_models/test_amenity.py'
        result = pep8style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

if __name__ == '__main__':
    unittest.main()
