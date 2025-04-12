#!/usr/bin/python3

"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    This class defines a Rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        if self.height == 0 or self.width == 0:
            return ""
        result = []
        for _ in range(self.height):
            result.append(str(self.print_symbol) * self.width)
        return "\n".join(result)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Delete the rectangle.
        """
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the bigger one.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
