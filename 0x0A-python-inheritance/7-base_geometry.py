#!/usr/bin/python3
"""Define a class BaseGeometry with an area method that raises an exception."""


class BaseGeometry:
    """A class that represents basic geometric operations."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
