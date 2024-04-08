#!/usr/bin/python3
"""Defines a Class Rectangle"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialises width and height when instance is created"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns width of instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method that sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns height of instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method that sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns area of instance"""
        return self.__height * self.__width

    def perimeter(self):
        """Method that returns perimeter of a instance"""
        if self.__width and self.__height:
            return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """Return a printable form of a rectangle"""
        if self.__width and self.__height:
            shape = []
            for i in range(self.__height):
                for j in range(self.__width):
                    shape.append("#")
                if i != self.__height - 1:
                    shape.append("\n")
            return ("".join(shape))

    def __repr__(self):
        """Return the string representation of instance"""
        shape = "Rectangle(" + str(self.__width)
        shape += ", " + str(self.__height) + ")"
        return shape

    def __del__(self):
        """Prints a message for every deletion of instance"""
        print("Bye rectangle...")
