#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class defines a square by its size."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @size.setter
    def size(self, size):
        """Set the size of the square."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, position):
        """Set the position of the square."""
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
            return
        print('\n' * self.__position[1], end='')
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)

    def __str__(self):
        """Return a string representation of the square."""
        if self.size == 0:
            return ""

        result = []
        for _ in range(self.__position[1]):
            result.append("")

        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(result)
