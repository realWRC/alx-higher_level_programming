#!/usr/bin/python3
"""
Module: 4-inherits_from.py
Contains function for checking for subclasses.
"""


def inherits_from(obj, a_class):
    """
    Function that checks if obj is a subclass of a_class
    compares obj and a_class.
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
