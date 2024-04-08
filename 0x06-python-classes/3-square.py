#!/usr/bin/python3
"""Defines an empty class called Square"""


class Square():
    """Class represents a square."""
    def __init__(self, size=0):
        """Initilising data and exception checking."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method that returns area"""
        return self.__size * self.__size
