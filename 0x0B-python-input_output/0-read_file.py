#!/usr/bin/python3
"""
Module: 0-read_file.py
Defines a functions for I/O.
"""


def read_file(filename=""):
    """
    Function that reads a text file and prints it to stdout.
    """
    with open(filename, mode="r", encoding="utf-8") as _file:
        data = _file.read()
        print(data, end="")
