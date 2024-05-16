#!/usr/bin/python3
"""
Module base: Defines class Base
"""

import json
import os


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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method that writes to a JSON file """
        if list_objs is None or list_objs == []:
            data = "[]"
        else:
            data = cls.to_json_string([x.to_dictionary() for x in list_objs])
        name = cls.__name__ + ".json"
        with open(name, 'w') as j_file:
            j_file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """ Converts JSON string to list """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates a copy of an instance """
        if type(dictionary) != dict:
            raise TypeError("dictionaray must be of type dict")
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Loads objects from JSON file """
        name = cls.__name__ + ".json"
        objects = []
        if os.path.exists(name):
            with open(name, 'r') as js_file:
                string = js_file.read()
            obj_list = cls.from_json_string(string)
            objects = []
            for obj in obj_list:
                objects.append(cls.create(**obj))
        return objects
