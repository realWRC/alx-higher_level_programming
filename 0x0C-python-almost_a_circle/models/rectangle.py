#!/usr/bin/python3
"""Module for Class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Defines the Class Rectangle which is a
    subclass of class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises and validates class info"""
        self.validate("width", width)
        self.validate("height", height)
        self.validate("x", x)
        self.validate("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter"""
        return self.__width

    @property
    def height(self):
        """Getter"""
        return self.__height

    @property
    def x(self):
        """Getter"""
        return self.__x

    @property
    def y(self):
        """Getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter"""
        self.validate("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter"""
        self.validate("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter"""
        self.validate("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter"""
        self.validate("y", value)
        self.__y = value

    @staticmethod
    def validate(attribute, value):
        """Validates attributes"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if (attribute == 'x' or attribute == 'y') and (value < 0):
            raise ValueError("{} must be >= 0".format(attribute))
        if (attribute == 'width' or attribute == 'height') and value <= 0:
            raise ValueError("{} must be > 0".format(attribute))
