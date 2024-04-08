#!/usr/bin/python3
"""Defines an empty class called Square"""


class Square():
    """Class represents a square."""
    def __init__(self, size=0):
        """Initilising data and exception checking."""
        self.__size = size

    def size(self):
        """Method that returns current size"""
        return self.__size
    
    def size(self, value):
        """Method that resets size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method that returns area"""
        return self.__size * self.__size
