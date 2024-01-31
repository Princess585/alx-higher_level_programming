#!/usr/bin/python3
"""Defines a text-indentation function"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'

    Args:
        text (string): The text to print
    Raises:
        TypeError: If text is not a str
    """
    if not isinstance(text, str):
        raise TypeError("The text must be a str")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1