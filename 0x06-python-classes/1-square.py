#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class defines a square by its size."""
    def __init__(self, size):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
