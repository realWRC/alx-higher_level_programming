#!/usr/bin/python3
"""
Module: 10-square.py
Contains definition of class Square
"""


Rectangle = __init__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a subclass of Rectangle Square"""

    def __init__(self, size):
        """Instantiates object of class Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
