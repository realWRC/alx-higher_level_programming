#!/usr/bin/python3
"""
Module base: Defines class Base
"""

import json


class Base:
    """The definition of clas base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises object of class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns a json string of class Base Object
        """
        return json.dumps(list_dictionaries)
