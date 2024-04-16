#!/usr/bin/python3
"""
Module: 3-to_json_string.py
Defines functions for handling JSON files.
"""


import json


def from_json_string(my_str):
    """
    Function that returns the python object representation
    of a JSON string.
    """
    return json.loads(my_str)
