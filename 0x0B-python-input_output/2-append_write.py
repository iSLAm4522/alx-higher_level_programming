#!/usr/bin/python3
"""
This module provides functionality for appending text to files.
It contains a function that appends text to a file and returns the number
of characters written.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number
    of characters added.

    :param filename: The path to the file where text will be appended
    :type filename: str
    :param text: The string to append to the file
    :type text: str
    :return: The number of characters written to the file
    :rtype: int
    """
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
