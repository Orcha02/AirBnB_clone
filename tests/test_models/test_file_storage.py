#!/usr/bin/python3
"""Test module"""


import pep8
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """New class to test class Amenity"""
    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        my_file_storage = FileStorage()
        self.assertIsInstance(my_file_storage, FileStorage)

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
