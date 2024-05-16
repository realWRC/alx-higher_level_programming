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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list of dictionries")
        if not all(type(element) == dict for element in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionries")
        return json.dumps(list_dictionaries)
