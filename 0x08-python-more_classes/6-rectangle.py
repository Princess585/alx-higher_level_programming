#!/usr/bin/python3
"""Defines a Rectangle of aclass"""


class Rectangle:
    """Represent a rect

    Attributes:
        number_of_instances (int): Number of Rect instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rect

        Args:
            width (int): Width of the new rect
            height (int): Height of the new rect
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rect"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("The width must be an int")
        if value < 0:
            raise ValueError("The width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rect"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("The height must be an int")
        if value < 0:
            raise ValueError("The height must be >= 0")
        self.__height = value

    def area(self):
        """Ret the area of the Rect"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Ret the perimeter of the Rect"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Ret the printable representation of the Rect

        Represents the rect with the # char
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Ret the str representation of the Rect"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Funct prints a message for every deletion of a Rect"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
