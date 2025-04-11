#!/usr/bin/python3

"""
Module 2-matrix_divided
Contains function matrix_divided that divides all elements of a matrix
"""


def matrix_divided(matrix, div):

    """Divides all elements of a matrix by a number.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number to divide the matrix elements by.
    Returns:
        list: A new matrix with all elements divided by div,
              rounded to 2 decimal places.
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                  if rows are not the same size,
                  or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    size = len(matrix[0])
    result = []
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )
            new_row.append(round(ele / div, 2))
        result.append(new_row)
    return result
