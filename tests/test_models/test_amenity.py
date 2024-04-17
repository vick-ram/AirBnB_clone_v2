#!/usr/bin/python3
"""
This module tests for amenity model class
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """This class initializes the test and it implements test_basemodel
    super class
    """

    def __init__(self, *args, **kwargs):
        """This function creates an initialization of test_amenity class
	It takes two arguments args and kwargs
	"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """This function tests for name and returns true if string type
	"""
        new = self.value()
        self.assertEqual(type(new.name), str)
