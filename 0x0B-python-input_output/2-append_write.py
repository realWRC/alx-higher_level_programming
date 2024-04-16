#!/usr/bin/python3
"""
Module: 0-read_file.py
Defines a functions for I/O.
"""


def append_write(filename="", text=""):
    """
    Function appends a string at the end of a text file
    and returns number of characters added.
    """
    with open(filename, mode='a', encoding="utf-8") as _file:
        return _file.write(text)
