#!/usr/bin/python3
"""
This module provides functionality for reading and printing text files.
It contains a function that reads a file and prints its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads and prints the content of a text file to the standard output.
    :param filename: The path to the file that needs to be read.
    :type filename: Str
    :return: None
    """
    with open(filename, "r", encoding="utf-8") as file:
        for chunk in file:
            print(chunk, end="")
