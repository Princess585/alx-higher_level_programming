#!/usr/bin/python3

"""Does exacly the same as python code"""

import math


class MagicClass:
    """Represent a circle"""

    def __init__(self, radius=0):
        """Initialize a MagicClass

        Arg:
            radius (float or int): Radius of the new MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("The radius must be a number")
        self.__radius = radius

    def area(self):
        """Ret an area of a MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Ret The circumference of the MagicClass"""
        return (2 * math.pi * self.__radius)
