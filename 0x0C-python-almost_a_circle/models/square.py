#!/usr/bin/python3
"""
Module: square.py
Contains class Square
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Instanciates class """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Returns attribute size """
        return self.__width

    @size.setter
    def size(self, value):
        """ Setter for attribute size """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """ Returns formatted string represention of instance attributes """
        string = "[Square] ({}) {}/{} - {}".format(
                 self.id, self.x, self.y, self.__width)
        return string
