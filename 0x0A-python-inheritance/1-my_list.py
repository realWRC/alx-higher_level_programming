#!/usr/bin/python3
"""
Module: 1-my_list.py
Contains the functions and classes that inherit from the
built-in list class.
"""


class MyList(list):
    """
    Child class MyList of parent built-in class list.
    """
    def print_sorted(self):
        _sorted = self[:]
        _sorted.sort()
        print("{}".format(_sorted))
