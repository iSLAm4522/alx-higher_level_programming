#!/usr/bin/python3

"""
    This function returns the list of available attributes and methods
    of an object.
    Args:
        obj: object
    Returns:
        list of attributes and methods
"""


class MyList(list):
    """MyList inherits from list"""
    def print_sorted(self):
        """Print the list in sorted order"""
        print(sorted(self))
