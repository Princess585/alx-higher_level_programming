#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): Size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("The size must be an integer")
        elif size < 0:
            raise ValueError("The size must be greater  >= 0")
        self.__size = size

    def area(self):
        """Ret current area of the square"""
        return (self.__size * self.__size)
