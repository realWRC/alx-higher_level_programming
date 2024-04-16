#!/usr/bin/python3
"""
Module: 3-to_json_string.py
Defines functions for handling JSON files.
"""


import json


def load_from_json_file(filename):
    """
    Function that returns the python object representation
    of a JSON string.
    """
    with open(filename, mode='r') as _file:
        data = _file.read()
        return json.loads(data)
