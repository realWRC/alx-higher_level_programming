#!/usr/bin/python3
""" Module: rectangle.py """


from models.base import Base


class Rectangle(Base):
    """ Defines child class of class Base Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instanstiates the Rectangle class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Returns attribute width """
        return self.__width

    @property
    def height(self):
        """ Returns attribute height """
        return self.__height

    @property
    def x(self):
        """ Returns attribute x """
        return self.__x

    @property
    def y(self):
        """ Returns attribute y """
        return self.__y

    @width.setter
    def width(self, value):
        """Setter for attribute width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for attribute height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for attribute x"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for attribute y"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method that return area """
        return self.__width * self.__height

    def display(self):
        """ Prints the object it # symbol """
        print("\n" * self.y, end="")
        for height in range(0, self.__height):
            for i in range(0, self.__x):
                print(" ", end="")
            for width in range(0, self.__width):
                print("#", end="")
            print()
