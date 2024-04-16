#!/usr/bin/python3
"""
Module: 0-read_file.py
Defines a functions for I/O.
"""


def write_file(filename="", text=""):
    """
    Function that writes to a text file and returns
    number of characters written.
    """
    with open(filename, mode='w+', encoding="utf-8") as _file:
        return _file.write(text)
