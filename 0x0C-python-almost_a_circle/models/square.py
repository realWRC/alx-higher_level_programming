#!/usr/bin/python3
""" Module: square.py """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines the subclass Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialises the class with superclass attributes """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ Prints the string representation of Square class """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
