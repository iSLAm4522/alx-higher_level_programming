#!/usr/bin/python3
"""
Module 0-add_integer
Contains function add_integer
"""


def add_integer(a, b=98):
    """
    Adds two integers
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
