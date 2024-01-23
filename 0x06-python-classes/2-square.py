#!/usr/bin/python3

"""Define a class of a Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square

        Args:
            size (int): Size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("The size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater than  >= 0")
        self.__size = size
