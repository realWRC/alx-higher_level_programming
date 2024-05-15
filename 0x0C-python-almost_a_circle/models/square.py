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
        self.validate("width", value)
        self.width = value
        self.validate("height", value)
        self.height = value

    def update(self, *args, **kwargs):
        """ Function that update Square """
        if args is not None:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns dictionary representation of class """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

    def __str__(self):
        """ Prints the string representation of Square class """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
