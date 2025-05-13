#!/usr/bin/python3
"""
Module for converting class instances to JSON-serializable dictionary
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class

    Returns:
        dict: Dictionary representation of the object
    """
    return obj.__dict__
