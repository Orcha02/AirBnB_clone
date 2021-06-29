"""Test module"""


import pep8
import unittest
from models.place import Place


class TestMyPlace(unittest.TestCase):
    """New class to test class Place"""

    def setUp(self):
        """Setting up"""
        self.my_place = Place()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.my_place

    def test_is_instance_str(self):
        """Check if attributes are of correct type str"""
        self.assertIsInstance(self.my_place.city_id, str)
        self.assertIsInstance(self.my_place.user_id, str)
        self.assertIsInstance(self.my_place.name, str)
        self.assertIsInstance(self.my_place.description, str)

    def test_is_instance_int(self):
        """Check if attributes are of correct type int"""
        self.assertIsInstance(self.my_place.number_rooms, int)
        self.assertIsInstance(self.my_place.number_bathrooms, int)
        self.assertIsInstance(self.my_place.max_guest, int)
        self.assertIsInstance(self.my_place.price_by_night, int)

    def test_is_instance_float(self):
        """Check if attributes are of correct type float"""
        self.assertIsInstance(self.my_place.latitude, float)
        self.assertIsInstance(self.my_place.longitude, float)

    def test_is_instance_list(self):
        """Check if attributes are of correct type """
        self.assertIsInstance(self.my_place.amenity_ids, list)

    def test_if_attrs_exist(self):
        """Check if attributes are present in the class"""
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_is_an_instance(self):
        """check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.my_place, Place)

    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(self.my_place.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)


class TestCodeFormat(unittest.TestCase):
    """Class to do pep8 validation."""
    def test_pep8(self):
        """Test that we conform to pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        file1 = 'models/place.py'
        file2 = 'tests/test_models/test_place.py'
        result = pep8style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

if __name__ == '__main__':
    unittest.main()
