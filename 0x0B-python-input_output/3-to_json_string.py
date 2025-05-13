#!/usr/bin/python3
"""Module for JSON string conversion.
Contains function to convert Python objects to JSON strings.
"""
import json


def to_json_string(my_obj):
    """Returns the JSON string representation of an object.

    Args:
        my_obj: Python object to be converted to JSON string

    Returns:
        str: JSON string representation of my_obj
    """
    return json.dumps(my_obj)
