#!/usr/bin/python3
"""
Module: 2-is_same_class.py
Contains function that compares two objects
"""

def is_same_class(obj, a_class):
    """
    Function that checks if object obj is of class
    a_class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
