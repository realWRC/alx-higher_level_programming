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
        self.size = size

    def size(self):
        """Method that returns current size"""
        return self.size

    def size(self, value):
        """Method that resets size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def area(self):
        """Method that returns area"""
        return self.size * self.size

    def my_print(self):
        """Method that prints the square"""
        if self.size:
            i = 0
            while i < self.size:
                j = 0
                while j < self.size:
                    print("#", end="")
                    j += 1
                print()
                i += 1
