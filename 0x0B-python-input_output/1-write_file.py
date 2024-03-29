#!/usr/bin/python3
"""Defines a file-writing funct"""


def write_file(filename="", text=""):
    """Write a str to a UTF8 text file

    Args:
        filename (str): The name of the file to write
        text (str): The text to write to the file
    Returns:
        The number of chars written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
