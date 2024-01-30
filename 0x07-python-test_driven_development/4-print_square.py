#!/usr/bin/python3
"""Defines a square-printing function"""


def print_square(size):
    """Print a square with the # char

    Args:
        size (int): The height/width of the square
    Raises:
        TypeError: If size is not an int
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("The size must be an integer")
    if size < 0:
        raise ValueError("The size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
