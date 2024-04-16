#!/usr/bin/python3
"""
Module: 9-student.py
Contains a class that defines a student.
"""


class Student:
    """Defines base class student"""

    def __init__(self, first_name, last_name, age):
        """Instantiates the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of Student"""
        return self.__dict__
