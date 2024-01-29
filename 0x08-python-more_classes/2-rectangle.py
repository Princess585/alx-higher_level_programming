#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represent a rec"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Args:
            width (int): Width of the new rec
            height (int): Height of the new rec
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rec"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("The width must be an integer")
        if value < 0:
            raise ValueError("The width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rec"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("The height must be an integer")
        if value < 0:
            raise ValueError("The height must be >= 0")
        self.__height = value

    def area(self):
        """Ret the area of the Rec"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Ret the perimeter of the Rec"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
