#!/usr/bin/python3
"""Test module"""


import unittest
from models.review import Review


class TestMyReview(unittest.TestCase):
    """New class to test class Review"""

    def setUp(self):
        """Setting up"""
        self.my_review = Review()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.my_review

    def test_is_instance(self):
        """Check if attributes are of a correct type"""
        self.assertIsInstance(self.my_review, Review)

    def test_if_str(self):
        """Check if the attrs are str"""
        self.assertIsInstance(self.my_review.place_id, str)
        self.assertIsInstance(self.my_review.user_id, str)
        self.assertIsInstance(self.my_review.text, str)

    def test_is_an_instance(self):
        """Check if my_model is an instance of BaseModel"""
        self.assertIsInstance(self.my_review, Review)

if __name__ == '__main__':
    unittest.main()
