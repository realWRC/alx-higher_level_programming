#!/usr/bin/python3
""" Module: base.py """


class Base:
    """ Defines a class base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiates object of class Base """
        if id is not None:
            if type(id) is not int:
                raise TypeError("id must be an integer")
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
