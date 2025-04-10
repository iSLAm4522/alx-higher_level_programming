#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class defines a square by its size."""
    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of the square."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size * self.size

    def __eq__(self, other):
        """Compare if two squares have the same area."""
        if not isinstance(other, Square):
            return False
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares have different areas."""
        if not isinstance(other, Square):
            return False
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare if this square's area is greater than another."""
        if not isinstance(other, Square):
            return False
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if this square's area is greater than or
            equal to another."""
        if not isinstance(other, Square):
            return False
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compare if this square's area is less than another."""
        if not isinstance(other, Square):
            return False
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if this square's area is less than or equal to another."""
        if not isinstance(other, Square):
            return False
        return self.area() <= other.area()
