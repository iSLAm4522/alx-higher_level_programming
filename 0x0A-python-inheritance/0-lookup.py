#!/usr/bin/python3

"""
    This function returns the list of available attributes and methods
    of an object.
    Args:
        obj: object
    Returns:
        list of attributes and methods
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    """
    return dir(obj)
