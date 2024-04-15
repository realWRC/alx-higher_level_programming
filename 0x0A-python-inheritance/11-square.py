#!/usr/bin/python3
"""
Module: 10-square.py
Contains definition of class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a subclass of Rectangle Square"""

    def __init__(self, size):
        """Instantiates object of class Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Prints string representation of class"""
        return (super().__str__())

    def area(self):
        """Returns the area of object"""
        return (self.__size ** 2)
