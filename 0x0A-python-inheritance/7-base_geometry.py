#!/usr/bin/python3
"""
Module: 5-base_geometry.py
Contains the definition of a Class
"""


class BaseGeometry:
    """
    Empty geometry class
    Methods to be added
    """
    def area(self):
        """
        Method that prints a message
        Strictky as a place holder
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value
        Using type function
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
