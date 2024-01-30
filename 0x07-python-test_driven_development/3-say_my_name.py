#!/usr/bin/python3
"""Defines a name-printing function"""


def say_my_name(first_name, last_name=""):
    """Print a name

    Args:
        first_name (str): The first name to print
        last_name (str): The last name to print
    Raises:
        TypeError: If either of first_name or last_name are not str
    """
    if not isinstance(first_name, str):
        raise TypeError("The first_name must be a str")
    if not isinstance(last_name, str):
        raise TypeError("The last_name must be a str")
    print("My name is {} {}".format(first_name, last_name))
