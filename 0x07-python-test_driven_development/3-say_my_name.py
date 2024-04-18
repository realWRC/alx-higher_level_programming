#!/usr/bin/python3
"""
This is function that prints two strings.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first_name to last_name.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
