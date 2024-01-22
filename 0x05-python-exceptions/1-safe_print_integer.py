#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer using "{:d}".format()

    Args:
        value (int): The integer to be printed

    Returns:
        True if value has been correctly printed and false if not
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
