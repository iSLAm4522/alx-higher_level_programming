#!/usr/bin/python3
"""Module for saving Python objects to JSON files"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON representation.

    Args:
        my_obj: The Python object to be serialized to JSON
        filename (str): The name of the file to write to

    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
