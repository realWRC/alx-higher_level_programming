#!/usr/bin/python3
"""
This module mainly defines a function that adds two
integers and returns the result.
"""
def add_integer(a, b=98):
    """
    Returns the sum of integers a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
