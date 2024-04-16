#!/usr/bin/python3
"""
Module: 3-to_json_string.py
Defines functions for handling JSON files.
"""


import json


def to_json_string(my_obj):
    """
    Function that returns the JSON string representation
    of a Python object.
    """
    return json.dumps(my_obj)
