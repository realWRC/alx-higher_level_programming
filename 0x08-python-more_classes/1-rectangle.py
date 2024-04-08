#!/usr/bin/python3
"""Defines a Class Rectangle"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialises width and height when instance is created"""
        self.width = width
        self.height = height

    def width(self):
        """Returns width of instance"""
        return self.__width

    def width(self, value):
        """Method that sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """Returns height of instance"""
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
