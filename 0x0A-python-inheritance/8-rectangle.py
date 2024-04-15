#!/usr/bin/python3
"""
Module: 8-rectangle.py
Defines child class Rectangle.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of child class rectangel."""
    def __init__(self, width, height):
        """Intantiates width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
