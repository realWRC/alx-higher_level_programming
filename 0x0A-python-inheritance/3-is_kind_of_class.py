#!/usr/bin/python3
"""
Module: 3-is_kind_of_class.py
Contains a function for checking instances.
"""


def is_kind_of_class(obj, a_class):
    """
    Function that checks is an instance of an object or any
    of its subclasses.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
