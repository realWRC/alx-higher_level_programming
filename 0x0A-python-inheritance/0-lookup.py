#!/usr/bin/python3
"""
Module: 0-lookup.py
This module defines contains functions that return a list
of the attributes and methods of a given class.
"""


def lookup(obj):
    """
    Function that returns a list of attributes and methods
    of a given class obj.
    """
    return dir(obj)
