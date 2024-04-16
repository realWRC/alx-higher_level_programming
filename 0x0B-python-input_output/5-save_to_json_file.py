#!/usr/bin/python3
"""
Module: 3-to_json_string.py
Defines functions for handling JSON files.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function that returns the python object representation
    of a JSON string.
    """
    with open(filename, mode='w+') as _file:
        _file.write(json.dumps(my_obj))
