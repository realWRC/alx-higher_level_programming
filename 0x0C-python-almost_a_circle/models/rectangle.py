#!/usr/bin/python3
"""Module: rectangle.py"""

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

    def area(self):
        """ Calculates the area of a rectangle """
        return self.__width * self.__height

    def display(self):
        """Print rectangle"""
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ Reassigns arguments """
        if args is not None:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Returns the dictionary representation of class"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}

    def __str__(self):
        """Returns string representation of class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)
