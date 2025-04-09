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

    def my_print(self):
        """Print the square using the character '#'."""
        if (self.size == 0):
            print()
        else:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print('#', end="")
                print()
